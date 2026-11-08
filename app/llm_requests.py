import requests

from config import LLM_API_URL, LLM_API_HEADERS, LLM_API_PAYLOAD


def make_request(prompt: str) -> dict:
    """
    Sends a request with prompt to an LLM.

    :param prompt: The prompt text.
    :return: The LLM response.
    """
    LLM_API_PAYLOAD["messages"][0]["content"] = prompt

    try:
        response = requests.post(
            url=LLM_API_URL,
            headers=LLM_API_HEADERS,
            json=LLM_API_PAYLOAD,
        )

        data = response.json()

    except Exception as e:
        print(f"Error: '{e.__class__.__name__}' during the LLM API request.")
        return {}

    return data
