from src.llm_eval.evaluator import contains_required_terms


def test_answer_contains_required_terms():
    result = contains_required_terms(
        "The API returned 404 because the user was not found.",
        ["404", "user", "not found"],
    )
    assert result.passed
    assert result.score == 1.0
