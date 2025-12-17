"""Prompt rendering engine using Jinja2 templates."""

from typing import Dict, Any, List, Optional
from jinja2 import Template, TemplateError, UndefinedError
from .models import PromptTemplate


class PromptEngine:
    """Renders prompt templates with variable substitution and validation.
    
    Uses Jinja2 for flexible string templating with variable substitution.
    Validates that all required input variables are provided before rendering.
    """
    
    def __init__(self):
        """Initialize the prompt engine."""
        self.templates_cache = {}
        self.rendered_history = []
    
    def render(
        self,
        template: PromptTemplate,
        variables: Dict[str, Any]
    ) -> str:
        """Render a prompt template with provided variables.
        
        Args:
            template: PromptTemplate instance containing the template string
            variables: Dictionary of variables to substitute
            
        Returns:
            Rendered prompt string
            
        Raises:
            ValueError: If required variables are missing
            TemplateError: If template rendering fails
        """
        self._validate_variables(template, variables)
        
        try:
            jinja_template = Template(template.template)
            rendered = jinja_template.render(variables)
            
            self.rendered_history.append({
                'template_name': template.name,
                'rendered_prompt': rendered,
                'variables_used': variables.copy()
            })
            
            return rendered
        except (TemplateError, UndefinedError) as e:
            raise TemplateError(f"Error rendering template {template.name}: {str(e)}")
    
    def _validate_variables(
        self,
        template: PromptTemplate,
        variables: Dict[str, Any]
    ) -> None:
        """Validate that all required variables are provided.
        
        Args:
            template: PromptTemplate instance
            variables: Dictionary of provided variables
            
        Raises:
            ValueError: If required variables are missing
        """
        missing = []
        for var in template.input_variables:
            if var not in variables or variables[var] is None:
                missing.append(var)
        
        if missing:
            raise ValueError(
                f"Missing required variables for template '{template.name}': {', '.join(missing)}"
            )
    
    def chain_prompts(
        self,
        templates: List[PromptTemplate],
        initial_variables: Dict[str, Any],
        output_key: str = 'output'
    ) -> str:
        """Chain multiple prompts, passing output of one as input to next.
        
        Args:
            templates: List of PromptTemplate instances in order
            initial_variables: Initial variables for the first template
            output_key: Key to use for storing rendered prompt in chain
            
        Returns:
            Final rendered prompt
            
        Raises:
            ValueError: If chaining fails
        """
        variables = initial_variables.copy()
        
        for template in templates:
            try:
                rendered = self.render(template, variables)
                variables[output_key] = rendered
            except Exception as e:
                raise ValueError(f"Error in prompt chain at template '{template.name}': {str(e)}")
        
        return variables.get(output_key, '')
    
    def get_render_history(self) -> List[Dict[str, Any]]:
        """Get history of rendered prompts.
        
        Returns:
            List of rendered prompt records
        """
        return self.rendered_history.copy()
    
    def clear_history(self) -> None:
        """Clear the rendered history."""
        self.rendered_history = []
