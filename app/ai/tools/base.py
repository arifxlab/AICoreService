"""
Base class for AI tools.
"""

from abc import ABC, abstractmethod

from app.ai.tools.tool_schema import ToolDefinition


class BaseTool(ABC):
    """
    Abstract base class for all AI tools.
    """

    @property
    @abstractmethod
    def definition(self) -> ToolDefinition:
        """
        Return metadata describing this tool.
        """
        pass

    @abstractmethod
    async def execute(
        self,
        arguments: str,
    ) -> str:
        """
        Execute the tool.
        """
        pass