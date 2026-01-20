from euriai.langchain import create_chat_model
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


def _get_env_api_key() -> Optional[str]:
    key = os.getenv("EURI_API_KEY")
    if key and isinstance(key, str):
        key = key.strip()
    return key or None


def get_chat_model(api_key: Optional[str] = None):
    """Create and return the Euriai chat model.

    Priority: explicit `api_key` argument -> `EURIAI_API_KEY` env var.
    Raises a ValueError with a clear message when no valid key is available.
    """
    key = None
    if api_key and isinstance(api_key, str) and api_key.strip():
        key = api_key.strip()
    else:
        key = _get_env_api_key()

    if not key or not isinstance(key, str):
        raise ValueError(
            "EURIAI_API_KEY not set. Please set the EURIAI_API_KEY environment variable or pass a valid api_key."
        )

    chat_model = create_chat_model(
        api_key=key,
        model="gpt-4.1-nano",
        temperature=0.7,
    )

    return chat_model


def generate_response(chat_model, prompt: str):
    response = chat_model.invoke(prompt)
    return response.content