"""
Date and time tool.
"""

from datetime import datetime

from app.ai.tools.base import AITool


class DateTimeTool(AITool):
    """
    Returns the current date and time.
    """

    name = "datetime"

    description = (
        "Returns the current system date and time."
    )

    async def execute(
        self,
        input_text: str,
    ) -> str:
        """
        Return current date and time.
        """

        return datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )