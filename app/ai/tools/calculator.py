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
        """
        Return calculator metadata.
        """

        return ToolDefinition(
            name="calculator",
            description="Evaluate mathematical expressions.",
            parameters={
                "expression": ToolParameter(
                    type="string",
                    description="Mathematical expression to evaluate.",
                )
            },
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