
import pytest

from src.llm_eval.evaluator import calculate_quality_report


@pytest.mark.parametrize(
    "response, expected_pass",
    [
        (
            "A 404 error means the requested resource could not be found.",
            True,
        ),
        (
            "A 200 status means everything was successful.",
            False,
        ),
        (
            "The requested resource was not found and the server returned 404.",
            True,
        ),
    ],
)
def test_404_prompt_quality(response, expected_pass):
    report = calculate_quality_report(
        answer=response,
        required_terms=["404", "not found"],
        forbidden_terms=["200"],
        reference_facts=[
    "404",
    "not found",

        ],
    )

    assert (report.overall >= 0.75) is expected_pass