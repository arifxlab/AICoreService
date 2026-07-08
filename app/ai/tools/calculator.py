"""
Calculator tool.
"""

from app.ai.tools.base import BaseTool
from app.ai.tools.tool_schema import (
    ToolDefinition,
    ToolParameter,
)


class CalculatorTool(BaseTool):
    """
    Performs basic mathematical calculations.
    """

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name="calculator",
            description="Evaluate a mathematical expression.",
            properties={
                "expression": ToolParameter(
                    type="string",
                    description="The mathematical expression to evaluate.",
                )
            },
            required=["expression"],
        )

    async def execute(
        self,
        arguments: str,
    ) -> str:
        """
        Execute calculation.
        """

        try:
            result = eval(
                arguments,
                {"__builtins__": {}},
                {},
            )

            return str(result)

        except Exception:
            return "Invalid mathematical expression."