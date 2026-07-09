"""
Registry for AI tools.
"""

from app.ai.tools.base import BaseTool
from app.ai.tools.calculator import CalculatorTool
from app.ai.tools.datetime_tool import DateTimeTool


class ToolRegistry:
    """
    Maintains a registry of all available AI tools.

    The registry provides methods to retrieve tools by name
    and to expose their definitions in the format expected by
    OpenAI/OpenRouter function calling APIs.
    """

    def __init__(self) -> None:
        """
        Initialize the available tools.
        """

        self._tools: dict[str, BaseTool] = {
            "calculator": CalculatorTool(),
            "datetime": DateTimeTool(),
        }

    def get(
        self,
        name: str,
    ) -> BaseTool | None:
        """
        Retrieve a tool by its registered name.

        Args:
            name: Name of the tool.

        Returns:
            The requested tool if found; otherwise None.
        """

        return self._tools.get(name)

    def all(
        self,
    ) -> dict[str, BaseTool]:
        """
        Return all registered tools.

        Returns:
            Dictionary containing all registered tools.
        """

        return self._tools

    def definitions(
        self,
    ) -> list[dict]:
        """
        Convert registered tools into the OpenAI/OpenRouter
        function-calling schema.

        Returns:
            A list of function definitions compatible with
            OpenAI/OpenRouter tool calling.
        """

        tool_definitions: list[dict] = []

        for tool in self._tools.values():
            schema = tool.definition

            tool_definitions.append(
                {
                    "type": "function",
                    "function": {
                        "name": schema.name,
                        "description": schema.description,
                        "parameters": {
                            "type": "object",
                            "properties": {
                                key: value.model_dump()
                                for key, value in schema.properties.items()
                            },
                            "required": schema.required,
                        },
                    },
                }
            )

        return tool_definitions
