"""Template loader for parsing YAML and JSON template files."""

import json
import yaml
from pathlib import Path
from typing import Dict, List, Optional
from .models import PromptTemplate


class TemplateLoader:
    """Loads and parses prompt templates from YAML/JSON files."""
    
    def __init__(self, template_dir: Optional[str] = None):
        """Initialize the template loader.
        
        Args:
            template_dir: Path to directory containing template files
        """
        self.template_dir = Path(template_dir) if template_dir else None
        self.templates_cache: Dict[str, PromptTemplate] = {}
    
    def load_template(self, file_path: str) -> PromptTemplate:
        """Load a single template from a YAML or JSON file.
        
        Args:
            file_path: Path to the template file
            
        Returns:
            PromptTemplate instance
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is invalid
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Template file not found: {file_path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            if path.suffix.lower() in ['.yaml', '.yml']:
                data = yaml.safe_load(f)
            elif path.suffix.lower() == '.json':
                data = json.load(f)
            else:
                raise ValueError(f"Unsupported file format: {path.suffix}")
        
        template = PromptTemplate(**data)
        self.templates_cache[template.name] = template
        return template
    
    def load_directory(self, directory: Optional[str] = None) -> Dict[str, PromptTemplate]:
        """Load all templates from a directory.
        
        Args:
            directory: Path to directory (uses instance template_dir if not provided)
            
        Returns:
            Dictionary of template name to PromptTemplate
        """
        target_dir = Path(directory) if directory else self.template_dir
        if not target_dir:
            raise ValueError("No directory specified")
        
        if not target_dir.is_dir():
            raise FileNotFoundError(f"Directory not found: {target_dir}")
        
        templates = {}
        for file_path in target_dir.glob('*.{yaml,yml,json}'):
            try:
                template = self.load_template(str(file_path))
                templates[template.name] = template
            except Exception as e:
                print(f"Error loading template from {file_path}: {e}")
        
        self.templates_cache.update(templates)
        return templates
    
    def get_template(self, name: str) -> Optional[PromptTemplate]:
        """Get a cached template by name.
        
        Args:
            name: Template name
            
        Returns:
            PromptTemplate or None if not found
        """
        return self.templates_cache.get(name)
    
    def list_templates(self) -> List[str]:
        """List all loaded template names.
        
        Returns:
            List of template names
        """
        return list(self.templates_cache.keys())
