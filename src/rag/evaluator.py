
from dataclasses import dataclass


@dataclass
class RAGResult:
    context_relevance: float
    faithfulness: float
    answer_correctness: float
    overall: float


def evaluate_rag(
    context: str,
    answer: str,
    expected_facts: list[str],
) -> RAGResult:
    context_lower = context.lower()
    answer_lower = answer.lower()

    relevant_facts = sum(
        fact.lower() in context_lower
        for fact in expected_facts
    )

    supported_facts = sum(
        fact.lower() in answer_lower and fact.lower() in context_lower
        for fact in expected_facts
    )

    context_relevance = (
        relevant_facts / len(expected_facts)
        if expected_facts
        else 1.0
    )

    faithfulness = (
        supported_facts / len(expected_facts)
        if expected_facts
        else 1.0
    )

    answer_correctness = (
        sum(fact.lower() in answer_lower for fact in expected_facts)
        / len(expected_facts)
        if expected_facts
        else 1.0
    )

    overall = (
        context_relevance
        + faithfulness
        + answer_correctness
    ) / 3

    return RAGResult(
        context_relevance=round(context_relevance, 2),
        faithfulness=round(faithfulness, 2),
        answer_correctness=round(answer_correctness, 2),
        overall=round(overall, 2),
    )