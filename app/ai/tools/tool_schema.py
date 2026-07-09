"""
Schema definitions for AI tools.
"""

from pydantic import BaseModel, Field


class ToolParameter(BaseModel):
    """
    Represents a single tool parameter.
    """

    type: str = Field(
        ...,
        description="Data type of the parameter.",
    )

    description: str = Field(
        ...,
        description="Description of the parameter.",
    )


class ToolDefinition(BaseModel):
    """
    Metadata describing an AI tool.
    """

    name: str = Field(
        ...,
        description="Unique tool name.",
    )

    description: str = Field(
        ...,
        description="Description of the tool.",
    )

    properties: dict[str, ToolParameter] = Field(
        default_factory=dict,
        description="Tool input parameters.",
    )

    required: list[str] = Field(
        default_factory=list,
        description="Required parameter names.",
    )
