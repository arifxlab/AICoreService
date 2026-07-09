"""
Base abstractions for AI tools.
"""

from abc import ABC, abstractmethod

from app.ai.tools.tool_schema import ToolDefinition


class BaseTool(ABC):
    """
    Abstract base class for all AI tools.

    Every tool must expose a metadata definition and implement
    asynchronous execution.
    """

    @property
    @abstractmethod
    def definition(self) -> ToolDefinition:
        """
        Return the metadata describing this tool.

        Returns:
            ToolDefinition: The tool's name, description,
            and parameter schema.
        """
        ...

    @abstractmethod
    async def execute(
        self,
        arguments: str,
    ) -> str:
        """
        Execute the tool.

        Args:
            arguments: Input arguments provided to the tool.

        Returns:
            str: The tool execution result.
        """
        ...