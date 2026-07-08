"""
Registry for AI tools.
"""

from app.ai.tools.base import AITool
from app.ai.tools.calculator import CalculatorTool
from app.ai.tools.datetime_tool import DateTimeTool


class ToolRegistry:
    """
    Stores available AI tools.
    """

    def __init__(self) -> None:
        self._tools: dict[str, AITool] = {
            "calculator": CalculatorTool(),
            "datetime": DateTimeTool(),
        }

    def get(
        self,
        name: str,
    ) -> AITool | None:
        """
        Retrieve tool by name.
        """

        return self._tools.get(name)

    def all(self) -> dict[str, AITool]:
        """
        Return all registered tools.
        """

        return self._tools