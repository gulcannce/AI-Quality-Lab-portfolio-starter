from dataclasses import dataclass


@dataclass
class EvalResult:
    passed: bool
    score: float
    reason: str


def contains_required_terms(answer: str, required_terms: list[str]) -> EvalResult:
    answer_lower = answer.lower()
    missing = [term for term in required_terms if term.lower() not in answer_lower]
    score = (len(required_terms) - len(missing)) / len(required_terms) if required_terms else 1.0
    return EvalResult(
        passed=not missing,
        score=score,
        reason="Missing terms: " + ", ".join(missing) if missing else "All required terms found",
    )
