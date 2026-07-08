"""
Tool schema definitions.
"""

from pydantic import BaseModel, Field


class ToolParameter(BaseModel):
    """
    Describes a single tool parameter.
    """

    type: str = Field(
        ...,
        description="Parameter type",
    )

    description: str = Field(
        ...,
        description="Parameter description",
    )


class ToolDefinition(BaseModel):
    """
    Metadata describing a tool.
    """

    name: str = Field(
        ...,
        description="Tool name",
    )

    description: str = Field(
        ...,
        description="Tool description",
    )

    parameters: dict[str, ToolParameter] = Field(
        default_factory=dict,
        description="Tool parameters",
    )