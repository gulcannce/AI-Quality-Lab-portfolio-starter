
from src.llm.client import LLMClient
from src.llm_eval.evaluator import calculate_quality_report


class FakeLLMClient(LLMClient):

    def __init__(self, response: str):
        self.response = response

    def generate(self, prompt: str) -> str:
        return self.response


def evaluate_response(response: str):
    return calculate_quality_report(
        answer=response,
        required_terms=["404", "user", "not found"],
        forbidden_terms=["200", "user found"],
        reference_facts=[
            "404",
            "user was not found",
        ],
    )


def test_good_llm_response_passes_quality_check():
    client = FakeLLMClient(
        "The API returned 404 because the user was not found."
    )

    response = client.generate("Explain a 404 error.")
    report = evaluate_response(response)

    assert report.overall >= 0.75
    assert report.groundedness >= 0.5


def test_bad_llm_response_fails_quality_check():
    client = FakeLLMClient(
        "The API returned 200 and the user was found successfully."
    )

    response = client.generate("Explain a 404 error.")
    report = evaluate_response(response)

    assert report.overall < 0.75