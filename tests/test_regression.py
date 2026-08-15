
from src.regression.gate import evaluate_regression


def test_quality_improvement_passes():
    result = evaluate_regression(
        baseline=0.85,
        current=0.91,
    )

    assert result.passed
    assert result.delta == 0.06


def test_quality_drop_fails():
    result = evaluate_regression(
        baseline=0.91,
        current=0.74,
    )

    assert not result.passed
    assert result.delta == -0.17


def test_score_below_threshold_fails():
    result = evaluate_regression(
        baseline=0.82,
        current=0.79,
    )

    assert not result.passed