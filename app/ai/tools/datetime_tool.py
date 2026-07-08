"""
Date and time tool.
"""

from datetime import datetime

from app.ai.tools.base import BaseTool
from app.ai.tools.tool_schema import ToolDefinition


class DateTimeTool(BaseTool):
    """
    Returns current system date and time.
    """

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name="datetime",
            description="Returns the current system date and time.",
            properties={},
            required=[],
        )

    async def execute(
        self,
        arguments: str,
    ) -> str:
        """
        Execute tool.
        """

        return datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )