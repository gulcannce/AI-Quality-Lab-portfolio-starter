import pytest

from src.agent.router import AgentRouter


@pytest.mark.parametrize(
    "intent, expected_tool, expected_id",
    [
        ("Find user 42", "get_user", "42"),
        ("Find user 7", "get_user", "7"),
        ("Delete user 42", "delete_user", "42"),
    ],
)
def test_agent_selects_correct_tool(intent, expected_tool, expected_id):
    router = AgentRouter()

    result = router.route(intent)

    assert result.tool == expected_tool
    assert result.arguments["id"] == expected_id


def test_agent_does_not_execute_unknown_intent():
    router = AgentRouter()

    result = router.route("Make me a coffee")

    assert result.tool == "unknown"
    assert result.arguments == {}