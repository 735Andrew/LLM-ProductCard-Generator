from json import loads
from pprint import pprint

from config import PRODUCT_PARAMETERS, SEO_PROMPT_LOCATION, PRODUCT_PROMPT_LOCATION
from app.llm_requests import make_request


def str_to_json(value: str) -> dict:
    """
    Convert a raw JSON string into a dictionary.

    :param value: The raw JSON string to convert.
    :return: The parsed product data.
    """

    try:
        return loads(value)
    except Exception as e:
        print(f"Error: '{e.__class__.__name__}' while converting string to JSON: '{e}'.")
        return {}


def create_prompt(product: dict) -> str:
    """
    Create a prompt for an LLM.

    :param product: The product details used to build the prompt.
    :return: Text of prompt.
    """

    with open(SEO_PROMPT_LOCATION, "r", encoding="utf-8") as f:
        context = f.read()

    with open(PRODUCT_PROMPT_LOCATION, "r", encoding="utf-8") as f:
        content = f.read() + str(product)

    return context + content


def report_output(output: dict) -> None:
    """
    Prepare and print the LLM API output to the terminal.

    :param output: The LLM API answer to the prompt.
    :return: None.
    """

    try:
        pprint(output["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"Error: '{e.__class__.__name__}' while printing LLM response.")
        pprint(output)


def run(products: list) -> None:
    """
    A service layer that processes data to and from the LLM.

    :param products: A list of raw JSON strings.
    :return: None.
    """

    for raw_data in products:
        product = str_to_json(raw_data)

        if not all(key in product for key in PRODUCT_PARAMETERS):
            print(f"Product: '{product}' is missing essential fields.")
            continue

        context_prompt = create_prompt(product)
        llm_report = make_request(context_prompt)

        if not llm_report:
            print(f"Empty or invalid LLM API response for product: '{product}'.")
            continue

        report_output(llm_report)
