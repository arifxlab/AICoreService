"""
Registry for AI tools.
"""

from app.ai.tools.base import BaseTool
from app.ai.tools.calculator import CalculatorTool
from app.ai.tools.datetime_tool import DateTimeTool


class ToolRegistry:
    """
    Stores available AI tools.
    """

    def __init__(self) -> None:

        self._tools: dict[str, BaseTool] = {
            "calculator": CalculatorTool(),
            "datetime": DateTimeTool(),
        }

    def get(
        self,
        name: str,
    ) -> BaseTool | None:

        return self._tools.get(name)

    def all(
        self,
    ) -> dict[str, BaseTool]:

        return self._tools

    def definitions(
        self,
    ) -> list[dict]:
        """
        Convert tools into OpenRouter/OpenAI function format.
        """

        definitions = []

        for tool in self._tools.values():

            schema = tool.definition

            definitions.append(
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

        return definitions