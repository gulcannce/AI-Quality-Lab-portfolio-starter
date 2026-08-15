
import os

import pytest

from src.llm.openai_client import OpenAIClient


@pytest.mark.integration
@pytest.mark.skipif(
    not os.getenv("RUN_LLM_INTEGRATION"),
    reason="Real LLM integration tests are disabled by default",
)
def test_openai_returns_response():
    client = OpenAIClient()

    response = client.generate(
        "Explain in one sentence what a 404 HTTP status code means."
    )

    assert response
    assert len(response) > 10