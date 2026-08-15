from dataclasses import dataclass


@dataclass
class ToolCall:
    tool: str
    arguments: dict


class AgentRouter:
    def route(self, intent: str) -> ToolCall:
        normalized = intent.lower()

        if "find user" in normalized:
            user_id = normalized.split("find user")[-1].strip()
            return ToolCall(
                tool="get_user",
                arguments={"id": user_id},
            )

        if "delete user" in normalized:
            user_id = normalized.split("delete user")[-1].strip()
            return ToolCall(
                tool="delete_user",
                arguments={"id": user_id},
            )

        return ToolCall(
            tool="unknown",
            arguments={},
        )