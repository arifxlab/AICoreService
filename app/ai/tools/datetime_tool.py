"""
Date and time tool.
"""

from datetime import datetime

from app.ai.tools.base import BaseTool
from app.ai.tools.tool_schema import ToolDefinition


class DateTimeTool(BaseTool):
    """
    Tool that returns the current system date and time.
    """

    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    @property
    def definition(self) -> ToolDefinition:
        """
        Return the tool definition.
        """

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
        Return the current date and time.

        The ``arguments`` parameter is accepted for consistency with the
        BaseTool interface but is not used by this tool.
        """

        return datetime.now().strftime(self.DATETIME_FORMAT)
