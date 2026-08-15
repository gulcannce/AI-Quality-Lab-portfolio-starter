
from dataclasses import dataclass


@dataclass
class RegressionResult:
    baseline: float
    current: float
    threshold: float
    passed: bool
    delta: float


def evaluate_regression(
    baseline: float,
    current: float,
    minimum_score: float = 0.80,
) -> RegressionResult:
    delta = round(current - baseline, 2)

    passed = (
        current >= minimum_score
        and current >= baseline
    )

    return RegressionResult(
        baseline=baseline,
        current=current,
        threshold=minimum_score,
        passed=passed,
        delta=delta,
    )