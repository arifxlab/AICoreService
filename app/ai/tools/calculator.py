"""
Calculator tool implementation.
"""

from typing import Any

from app.ai.tools.base import BaseTool
from app.ai.tools.tool_schema import (
    ToolDefinition,
    ToolParameter,
)


class CalculatorTool(BaseTool):
    """
    Tool for evaluating simple mathematical expressions.
    """

    @property
    def definition(self) -> ToolDefinition:
        """
        Return the calculator tool definition.
        """

        return ToolDefinition(
            name="calculator",
            description="Evaluate a mathematical expression.",
            properties={
                "expression": ToolParameter(
                    type="string",
                    description="The mathematical expression to evaluate.",
                ),
            },
            required=["expression"],
        )

    async def execute(
        self,
        arguments: str,
    ) -> str:
        """
        Evaluate a mathematical expression.

        Args:
            arguments: Mathematical expression supplied by the user.

        Returns:
            Result of the evaluated expression or an error message.
        """

        safe_globals: dict[str, Any] = {
            "__builtins__": {},
        }

        try:
            result = eval(arguments, safe_globals, {})
            return str(result)

        except Exception:
            return "Invalid mathematical expression."
