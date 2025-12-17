#!/usr/bin/env python3
"""Examples demonstrating the Prompt Engineering Framework.

This module shows how to use the framework with 10 example templates covering
all five required prompt engineering patterns.
"""

from prompt_engine import PromptTemplate, PromptEngine


# ============================================================================
# ZERO-SHOT PATTERNS (Direct instructions)
# ============================================================================

def example_zero_shot_qa():
    """Zero-shot Q&A template."""
    template = PromptTemplate(
        name="zero_shot_qa",
        description="Simple Q&A template for answering questions directly",
        template="Answer the following question: {{ question }}",
        input_variables=["question"]
    )
    
    engine = PromptEngine()
    result = engine.render(template, {"question": "What is machine learning?"})
    print("Zero-Shot Q&A:")
    print(result)
    print()


def example_zero_shot_summarize():
    """Zero-shot summarization template."""
    template = PromptTemplate(
        name="zero_shot_summarize",
        description="Template for summarizing text directly",
        template="Summarize the following text in 2-3 sentences:\n{{ text }}",
        input_variables=["text"]
    )
    
    engine = PromptEngine()
    result = engine.render(
        template,
        {"text": "Machine learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed."}
    )
    print("Zero-Shot Summarize:")
    print(result)
    print()


# ============================================================================
# FEW-SHOT PATTERNS (Learning from examples)
# ============================================================================

def example_few_shot_sentiment():
    """Few-shot sentiment analysis template."""
    examples = [
        {"text": "I loved this movie!", "sentiment": "positive"},
        {"text": "This was terrible.", "sentiment": "negative"},
        {"text": "It was okay.", "sentiment": "neutral"}
    ]
    
    template = PromptTemplate(
        name="few_shot_sentiment",
        description="Few-shot sentiment analysis with examples",
        template="Classify the sentiment of the following text:\n\n{{ examples_str }}\n\nText: {{ text }}\nSentiment:",
        input_variables=["text", "examples_str"],
        examples=examples
    )
    
    examples_str = "\n".join([f"Text: {e['text']}\nSentiment: {e['sentiment']}" for e in examples])
    
    engine = PromptEngine()
    result = engine.render(
        template,
        {"text": "This product exceeded my expectations!", "examples_str": examples_str}
    )
    print("Few-Shot Sentiment:")
    print(result)
    print()


def example_few_shot_translation():
    """Few-shot translation template."""
    examples = [
        {"english": "Hello", "spanish": "Hola"},
        {"english": "Thank you", "spanish": "Gracias"},
        {"english": "Good morning", "spanish": "Buenos días"}
    ]
    
    template = PromptTemplate(
        name="few_shot_translation",
        description="Few-shot English to Spanish translation",
        template="Translate the following English text to Spanish:\n\n{{ examples_str }}\n\nEnglish: {{ english_text }}\nSpanish:",
        input_variables=["english_text", "examples_str"],
        examples=examples
    )
    
    examples_str = "\n".join([f"English: {e['english']}\nSpanish: {e['spanish']}" for e in examples])
    
    engine = PromptEngine()
    result = engine.render(
        template,
        {"english_text": "How are you?", "examples_str": examples_str}
    )
    print("Few-Shot Translation:")
    print(result)
    print()


# ============================================================================
# CHAIN-OF-THOUGHT PATTERNS (Step-by-step reasoning)
# ============================================================================

def example_cot_math():
    """Chain-of-Thought math problem solving."""
    template = PromptTemplate(
        name="cot_math",
        description="Step-by-step math problem solving",
        template="""Solve this math problem step by step:

Problem: {{ problem }}

Step 1: Understand the problem
Step 2: Identify the approach
Step 3: Calculate
Step 4: Verify the answer

Answer:""",
        input_variables=["problem"]
    )
    
    engine = PromptEngine()
    result = engine.render(
        template,
        {"problem": "If a book costs $15 and you buy 3 books with a 10% discount, how much do you pay?"}
    )
    print("Chain-of-Thought Math:")
    print(result)
    print()


def example_cot_logic():
    """Chain-of-Thought logical reasoning."""
    template = PromptTemplate(
        name="cot_logic",
        description="Step-by-step logical reasoning",
        template="""Solve this logic puzzle step by step:

Puzzle: {{ puzzle }}

Let's think through this:
1. What do we know?
2. What can we deduce?
3. What's the conclusion?

Answer:""",
        input_variables=["puzzle"]
    )
    
    engine = PromptEngine()
    result = engine.render(
        template,
        {"puzzle": "All birds can fly. Penguins are birds. Can penguins fly?"}
    )
    print("Chain-of-Thought Logic:")
    print(result)
    print()


# ============================================================================
# ROLE-BASED PATTERNS (Persona-based prompting)
# ============================================================================

def example_role_expert():
    """Role-based expert assistant."""
    template = PromptTemplate(
        name="role_expert",
        description="Prompt that assigns an expert role",
        template="""You are an expert {{ expertise }} with {{ years }} years of experience.

Question: {{ question }}

Provide a detailed answer based on your expertise:""",
        input_variables=["expertise", "years", "question"]
    )
    
    engine = PromptEngine()
    result = engine.render(
        template,
        {
            "expertise": "software engineer",
            "years": "10",
            "question": "What are best practices for code review?"
        }
    )
    print("Role-Based Expert:")
    print(result)
    print()


def example_role_student():
    """Role-based student learner."""
    template = PromptTemplate(
        name="role_student",
        description="Prompt that uses student perspective",
        template="""Imagine you are a {{ level }} student learning {{ subject }}.

Explain in simple terms: {{ topic }}""",
        input_variables=["level", "subject", "topic"]
    )
    
    engine = PromptEngine()
    result = engine.render(
        template,
        {
            "level": "high school",
            "subject": "physics",
            "topic": "Newton's Third Law of Motion"
        }
    )
    print("Role-Based Student:")
    print(result)
    print()


# ============================================================================
# STRUCTURED OUTPUT PATTERNS (Formatted responses)
# ============================================================================

def example_structured_json():
    """Structured JSON output template."""
    template = PromptTemplate(
        name="structured_json",
        description="Template for structured JSON output",
        template="""Extract information from the text and return as JSON:

Text: {{ text }}

Return the response in this JSON format:
{"entities": [], "sentiment": "", "summary": ""}

JSON Response:""",
        input_variables=["text"]
    )
    
    engine = PromptEngine()
    result = engine.render(
        template,
        {"text": "The AI conference was amazing. I met brilliant researchers discussing neural networks."}
    )
    print("Structured JSON:")
    print(result)
    print()


def example_structured_list():
    """Structured list output template."""
    template = PromptTemplate(
        name="structured_list",
        description="Template for structured list output",
        template="""Generate a list of {{ count }} {{ item_type }} related to {{ topic }}.

Format each item as: - Item_Name: Description

Output:""",
        input_variables=["count", "item_type", "topic"]
    )
    
    engine = PromptEngine()
    result = engine.render(
        template,
        {"count": "3", "item_type": "machine learning algorithms", "topic": "classification"}
    )
    print("Structured List:")
    print(result)
    print()


# ============================================================================
# PROMPT CHAINING EXAMPLE
# ============================================================================

def example_prompt_chaining():
    """Demonstrate prompt chaining functionality."""
    
    # First template: Extract key points
    template1 = PromptTemplate(
        name="extract_key_points",
        description="Extract key points from text",
        template="Extract 3 key points from: {{ text }}",
        input_variables=["text"]
    )
    
    # Second template: Summarize key points
    template2 = PromptTemplate(
        name="summarize_points",
        description="Summarize the key points",
        template="Summarize these points into one sentence: {{ output }}",
        input_variables=["output"]
    )
    
    engine = PromptEngine()
    
    # Chain the templates
    initial_text = "Machine learning enables computers to learn from data. Deep learning uses neural networks. AI applications are transforming industries."
    
    result = engine.chain_prompts(
        [template1, template2],
        {"text": initial_text},
        output_key="output"
    )
    
    print("Prompt Chaining (Final Output):")
    print(result)
    print()


# ============================================================================
# INPUT VALIDATION EXAMPLE
# ============================================================================

def example_input_validation():
    """Demonstrate input validation."""
    template = PromptTemplate(
        name="question_answering",
        description="Answer questions",
        template="Q: {{ question }}\nA:",
        input_variables=["question"]
    )
    
    engine = PromptEngine()
    
    # This should work
    try:
        result = engine.render(template, {"question": "What is AI?"})
        print("Valid Input - Success:")
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    
    print()
    
    # This should fail - missing required variable
    try:
        result = engine.render(template, {})
        print("No Input - Success (unexpected)")
    except ValueError as e:
        print(f"No Input - Expected Error: {e}")
    print()


def main():
    """Run all examples."""
    print("="*70)
    print("PROMPT ENGINEERING FRAMEWORK - EXAMPLES")
    print("="*70)
    print()
    
    # Zero-Shot Examples
    print("\n--- ZERO-SHOT PATTERNS ---\n")
    example_zero_shot_qa()
    example_zero_shot_summarize()
    
    # Few-Shot Examples
    print("\n--- FEW-SHOT PATTERNS ---\n")
    example_few_shot_sentiment()
    example_few_shot_translation()
    
    # Chain-of-Thought Examples
    print("\n--- CHAIN-OF-THOUGHT PATTERNS ---\n")
    example_cot_math()
    example_cot_logic()
    
    # Role-Based Examples
    print("\n--- ROLE-BASED PATTERNS ---\n")
    example_role_expert()
    example_role_student()
    
    # Structured Output Examples
    print("\n--- STRUCTURED OUTPUT PATTERNS ---\n")
    example_structured_json()
    example_structured_list()
    
    # Advanced Features
    print("\n--- ADVANCED FEATURES ---\n")
    example_prompt_chaining()
    example_input_validation()
    
    print("="*70)
    print("All examples completed successfully!")
    print("="*70)


if __name__ == "__main__":
    main()
