# Prompt Engineering Framework

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A reusable Python library for creating, managing, and rendering dynamic LLM prompts from templates. This framework provides a robust system for handling complex prompt engineering patterns used in modern AI applications.

## Features

✨ **Core Capabilities:**
- 📝 **Template Definition**: Define prompts using YAML/JSON with metadata
- 🔄 **Variable Substitution**: Jinja2-based dynamic template rendering
- ✅ **Input Validation**: Automatic validation of required template variables
- 🔗 **Prompt Chaining**: Chain multiple prompts to create complex workflows
- 📚 **Template Loading**: Load templates from directories (YAML/JSON)
- 📊 **Render History**: Track and retrieve all rendered prompts

🎯 **Supported Prompt Patterns:**
1. **Zero-Shot**: Direct instructions/questions without examples
2. **Few-Shot**: Learning from provided examples
3. **Chain-of-Thought (CoT)**: Step-by-step reasoning prompts
4. **Role-Based**: Persona-based prompting
5. **Structured Output**: Prompts requiring specific format responses

## Installation

### From Source
```bash
git clone https://github.com/Kishorekalingi/prompt-engineering-framework.git
cd prompt-engineering-framework
pip install -e .
```

### Requirements
- Python 3.8+
- pydantic >= 2.0
- jinja2 >= 3.0
- pyyaml >= 6.0

## Quick Start

### Basic Usage

```python
from prompt_engine import PromptTemplate, PromptEngine

# Create a template
template = PromptTemplate(
    name="zero_shot_qa",
    description="Simple Q&A template",
    template="Answer the following question: {{ question }}",
    input_variables=["question"]
)

# Render the template
engine = PromptEngine()
result = engine.render(template, {"question": "What is machine learning?"})
print(result)
```

### Few-Shot Pattern Example

```python
template = PromptTemplate(
    name="sentiment_analysis",
    description="Classify sentiment using examples",
    template="""Classify the sentiment:

{{ examples_str }}

Text: {{ text }}
Sentiment:""",
    input_variables=["text", "examples_str"],
    examples=[
        {"text": "Great product!", "sentiment": "positive"},
        {"text": "Terrible experience", "sentiment": "negative"}
    ]
)

examples_str = "\n".join([f"Text: {e['text']}\nSentiment: {e['sentiment']}" 
                         for e in template.examples])
result = engine.render(template, {
    "text": "Amazing service!",
    "examples_str": examples_str
})
```

### Chain-of-Thought Example

```python
template1 = PromptTemplate(
    name="extract_key_points",
    description="Extract key points",
    template="Extract 3 key points from: {{ text }}",
    input_variables=["text"]
)

template2 = PromptTemplate(
    name="summarize",
    description="Summarize points",
    template="Summarize in one sentence: {{ output }}",
    input_variables=["output"]
)

# Chain templates
result = engine.chain_prompts(
    [template1, template2],
    {"text": "Your text here..."},
    output_key="output"
)
```

### Role-Based Pattern

```python
template = PromptTemplate(
    name="expert_assistant",
    description="Act as an expert",
    template="""You are an expert {{ expertise }}.

Question: {{ question }}

Provide detailed guidance:""",
    input_variables=["expertise", "question"]
)

result = engine.render(template, {
    "expertise": "Python developer",
    "question": "How to optimize list comprehensions?"
})
```

### Structured Output Pattern

```python
template = PromptTemplate(
    name="extract_json",
    description="Extract as JSON",
    template="""Extract information as JSON:

Text: {{ text }}

Return JSON format: {"entities": [], "sentiment": ""}

Response:""",
    input_variables=["text"]
)

result = engine.render(template, {
    "text": "Apple announced new products today."
})
```

## API Reference

### PromptTemplate

```python
PromptTemplate(
    name: str,                              # Unique template identifier
    description: str,                       # Template purpose description
    template: str,                          # Jinja2 template string
    input_variables: List[str],            # Required variable names
    examples: Optional[List[Dict]] = None, # Few-shot examples
    metadata: Optional[Dict] = None        # Additional metadata
)
```

### PromptEngine

```python
engine = PromptEngine()

# Render a template
result = engine.render(
    template: PromptTemplate,
    variables: Dict[str, Any]
) -> str

# Chain multiple templates
result = engine.chain_prompts(
    templates: List[PromptTemplate],
    initial_variables: Dict[str, Any],
    output_key: str = 'output'
) -> str

# Get render history
history = engine.get_render_history() -> List[Dict]

# Clear history
engine.clear_history()
```

### TemplateLoader

```python
loader = TemplateLoader(template_dir="./templates")

# Load single template
template = loader.load_template("path/to/template.yaml")

# Load all templates from directory
templates = loader.load_directory()

# Get cached template
template = loader.get_template("template_name")

# List all loaded templates
names = loader.list_templates() -> List[str]
```

## Template File Format

### YAML Format
```yaml
name: zero_shot_qa
description: Simple Q&A template
template: |
  Answer the following question: {{ question }}
input_variables:
  - question
metadata:
  category: QA
  difficulty: easy
```

### JSON Format
```json
{
  "name": "zero_shot_qa",
  "description": "Simple Q&A template",
  "template": "Answer the following question: {{ question }}",
  "input_variables": ["question"],
  "metadata": {
    "category": "QA",
    "difficulty": "easy"
  }
}
```

## Error Handling

```python
from prompt_engine import PromptEngine, PromptTemplate

engine = PromptEngine()
template = PromptTemplate(
    name="test",
    description="Test template",
    template="Question: {{ question }}",
    input_variables=["question"]
)

try:
    # This will fail - missing required variable
    result = engine.render(template, {})
except ValueError as e:
    print(f"Validation error: {e}")
    # Output: "Missing required variables for template 'test': question"
```

## Examples

Run the comprehensive examples:
```bash
python examples.py
```

This demonstrates:
- ✅ 2 Zero-shot patterns
- ✅ 2 Few-shot patterns
- ✅ 2 Chain-of-Thought patterns
- ✅ 2 Role-based patterns
- ✅ 2 Structured output patterns
- ✅ Prompt chaining
- ✅ Input validation

## Project Structure

```
prompt-engineering-framework/
├── prompt_engine/
│   ├── __init__.py           # Package initialization
│   ├── models.py             # Pydantic data models
│   ├── engine.py             # Jinja2 rendering engine
│   └── loader.py             # YAML/JSON template loader
├── examples.py               # 10 comprehensive examples
├── setup.py                  # Package configuration
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Use Cases

- 🤖 **LLM Applications**: Dynamic prompt generation for AI models
- 💬 **Chatbots**: Multi-turn conversation management
- 📊 **Data Processing**: Template-based text extraction
- 🔍 **Classification**: Few-shot learning for categorization
- 🧠 **Reasoning**: Chain-of-thought prompting for complex tasks
- 📝 **Content Generation**: Template-based content creation

## Design Principles

1. **Simplicity**: Easy-to-use API for common use cases
2. **Flexibility**: Support for diverse prompt engineering patterns
3. **Validation**: Automatic input validation with clear error messages
4. **Extensibility**: Easy to extend with custom patterns
5. **Performance**: Efficient template caching and rendering

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

MIT License - see LICENSE file for details

## Author

Kishore Kalingi (Student Developer)
B.Tech Student | Full-Stack Developer | Blockchain Enthusiast

## Acknowledgments

- Built with [Jinja2](https://jinja.palletsprojects.com/) for powerful templating
- Data validation using [Pydantic](https://docs.pydantic.dev/)
- Configuration parsing with [PyYAML](https://pyyaml.org/)

---

**Status**: ✅ Production Ready | **Last Updated**: December 2025
