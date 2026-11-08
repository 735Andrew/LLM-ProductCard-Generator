from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

LLM_API_TOKEN = os.environ.get("LLM_API_TOKEN")

PRODUCT_PARAMETERS = ["name", "manufacturer", "specs", "description"]

LLM_API_URL = "https://api.atria-asi.ai/v1/chat/completions"

LLM_API_HEADERS = {
    "Authorization": f"Bearer {LLM_API_TOKEN}",
    "Content-Type": "application/json",
}

LLM_API_PAYLOAD = {
    "model": "Atria-Dawn",
    "messages": [
        {
            "role": "user",
            "content": {}, # placeholder for prompt
        }
    ],
    "temperature": 0.3
}

SEO_PROMPT_LOCATION = fr"{basedir}\app\static\seo_prompt.md"
PRODUCT_PROMPT_LOCATION = fr"{basedir}\app\static\product_prompt.md"
