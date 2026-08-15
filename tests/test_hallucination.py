import pytest

from src.llm_eval.evaluator import calculate_quality_report


@pytest.mark.parametrize(
    "answer, expected_pass",
    [
        ("The capital of Turkey is Ankara.", True),
        ("The capital of Turkey is Istanbul.", False),
        ("Turkey's capital city is Ankara.", True),
        ("Turkey has no official capital.", False),
    ],
)
def test_hallucination_detection(answer, expected_pass):
    report = calculate_quality_report(
        answer=answer,
        required_terms=["Ankara"],
        forbidden_terms=["Istanbul", "no official capital"],
        reference_facts=["Ankara is the capital of Turkey"],
    )

    assert (report.overall >= 0.75) is expected_pass