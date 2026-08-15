import os

import pytest
from dotenv import load_dotenv

from src.api.client import ApiClient


load_dotenv()


@pytest.fixture
def api():
    base_url = os.getenv("BASE_URL")

    if not base_url:
        raise RuntimeError("BASE_URL environment variable is not set")

    return ApiClient(base_url)
