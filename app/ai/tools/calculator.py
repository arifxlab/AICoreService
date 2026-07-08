"""
Calculator tool.
"""

from app.ai.tools.base import AITool


class CalculatorTool(AITool):
    """
    Performs basic mathematical calculations.
    """

    name = "calculator"

    description = (
        "Evaluate simple mathematical expressions."
    )

    async def execute(
        self,
        input_text: str,
    ) -> str:
        """
        Execute calculation.
        """

        try:
            result = eval(
                input_text,
                {"__builtins__": {}},
                {},
            )

            return str(result)

        except Exception:
            return "Invalid mathematical expression."