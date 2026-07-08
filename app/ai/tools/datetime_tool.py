"""
Date and time tool.
"""

from datetime import datetime

from app.ai.tools.base import BaseTool
from app.ai.tools.tool_schema import (
    ToolDefinition,
    ToolParameter,
)


class DateTimeTool(BaseTool):
    """
    Returns the current date and time.
    """

    @property
    def definition(self) -> ToolDefinition:
        """
        Return datetime tool metadata.
        """

        return ToolDefinition(
            name="datetime",
            description="Returns the current system date and time.",
            parameters={},
        )

    async def execute(
        self,
        arguments: str,
    ) -> str:
        """
        Return current date and time.
        """

        return datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )