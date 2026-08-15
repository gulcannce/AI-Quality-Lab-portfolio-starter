import pytest

from src.rag.evaluator import evaluate_rag


@pytest.mark.parametrize(
    "context, answer, expected_pass",
    [
        (
            "The company headquarters is located in Ankara.",
            "The company headquarters is located in Ankara.",
            True,
        ),
        (
            "The company headquarters is located in Ankara.",
            "The company headquarters is located in Istanbul.",
            False,
        ),
        (
            "The company headquarters is located in Ankara.",
            "The company headquarters is located in Ankara and was founded in 1995.",
            True,
        ),
    ],
)
def test_rag_quality(context, answer, expected_pass):
    result = evaluate_rag(
        context=context,
        answer=answer,
        expected_facts=["company headquarters is located in Ankara"],
    )

    assert (result.overall >= 0.66) is expected_pass