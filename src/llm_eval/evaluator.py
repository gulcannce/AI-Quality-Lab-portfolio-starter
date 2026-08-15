from dataclasses import dataclass


@dataclass
class EvalResult:
    passed: bool
    score: float
    reason: str


@dataclass
class QualityReport:
    accuracy: float
    relevance: float
    completeness: float
    groundedness: float
    overall: float


def contains_required_terms(
    answer: str,
    required_terms: list[str],
) -> EvalResult:
    answer_lower = answer.lower()

    missing = [
        term
        for term in required_terms
        if term.lower() not in answer_lower
    ]

    score = (
        (len(required_terms) - len(missing))
        / len(required_terms)
        if required_terms
        else 1.0
    )

    return EvalResult(
        passed=not missing,
        score=score,
        reason=(
            f"Missing terms: {', '.join(missing)}"
            if missing
            else "All required terms found"
        ),
    )


def calculate_quality_report(
    answer: str,
    required_terms: list[str],
    forbidden_terms: list[str],
    reference_facts: list[str],
) -> QualityReport:
    answer_lower = answer.lower()

    required_found = sum(
        term.lower() in answer_lower
        for term in required_terms
    )

    forbidden_found = sum(
        term.lower() in answer_lower
        for term in forbidden_terms
    )

    grounded_facts = sum(
        fact.lower() in answer_lower
        for fact in reference_facts
    )

    accuracy = (
        (required_found - forbidden_found) / len(required_terms)
        if required_terms
        else 1.0
    )
    accuracy = max(0.0, min(1.0, accuracy))

    relevance = (
        required_found / len(required_terms)
        if required_terms
        else 1.0
    )

    completeness = relevance

    groundedness = (
        grounded_facts / len(reference_facts)
        if reference_facts
        else 1.0
    )

    overall = (
        accuracy
        + relevance
        + completeness
        + groundedness
    ) / 4

    return QualityReport(
        accuracy=round(accuracy, 2),
        relevance=round(relevance, 2),
        completeness=round(completeness, 2),
        groundedness=round(groundedness, 2),
        overall=round(overall, 2),
    )
