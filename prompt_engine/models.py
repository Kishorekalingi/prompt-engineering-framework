"""Pydantic models for prompt template schema validation."""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class PromptTemplate(BaseModel):
    """Data model for prompt templates with validation.
    
    Attributes:
        name: Unique identifier for the template
        description: Description of the template's purpose
        template: The template string with Jinja2 variables
        input_variables: List of required input variable names
        examples: Optional list of examples for few-shot patterns
    """
    
    name: str = Field(
        ...,
        description="Unique name for the template",
        min_length=1,
        max_length=255
    )
    
    description: str = Field(
        ...,
        description="Description of what the template does",
        min_length=1,
        max_length=1000
    )
    
    template: str = Field(
        ...,
        description="The prompt template string with Jinja2 variables",
        min_length=1
    )
    
    input_variables: List[str] = Field(
        default_factory=list,
        description="List of required input variable names"
    )
    
    examples: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="Optional examples for few-shot patterns"
    )
    
    metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional metadata about the template"
    )
    
    def model_dump_json(self) -> str:
        """Export template as JSON string."""
        return super().model_dump_json()
    
    class Config:
        """Pydantic model configuration."""
        json_schema_extra = {
            "example": {
                "name": "zero_shot_qa",
                "description": "Simple Q&A template",
                "template": "Answer the following question: {{ question }}",
                "input_variables": ["question"]
            }
        }
