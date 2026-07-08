import os
import sys

# Ensure parent directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import Agent
from agent.validator import Validator
from agent.router import Router
from agent.verifier import Verifier
from agent.memory import Memory
from tools.calculator import Calculator
from tools.keyword_extractor import KeywordExtractor
from tools.text_statistics import TextStatistics

def test_validator():
    print("--- Running Validator Tests ---")
    validator = Validator()
    test_cases = [
        ("", False),
        ("Hi", False),
        (123, False),
        ("Calculate 25+15", True)
    ]
    for q, expected in test_cases:
        valid, msg = validator.validate(q)
        print(f"Query: {repr(q)} -> Valid: {valid} ({msg})")
        assert valid == expected, f"Validator failed for query: {q}"

def test_router():
    print("\n--- Running Router Tests ---")
    router = Router()
    test_cases = {
        "Calculate 20 + 10": "calculator",
        "Extract keywords from this paragraph": "keywords",
        "Analyze this text": "statistics",
        "Hello, how are you?": "general"
    }
    for q, expected in test_cases.items():
        intent = router.route(q)
        print(f"Query: {repr(q)} -> Intent: {intent}")
        assert intent == expected, f"Router failed for query: {q}"

def test_tools():
    print("\n--- Running Tool Tests ---")
    # Calculator
    calc = Calculator()
    expr = "(10+5)*3"
    result = calc.evaluate(expr)
    print(f"Calculator: '{expr}' -> {result}")
    assert result == 45, "Calculator test failed"

    # Keyword Extractor
    extractor = KeywordExtractor()
    text = "Agentic AI systems use tools, memory, reasoning, and planning."
    keywords = extractor.extract(text, top_k=3)
    print(f"Keyword Extractor: '{text[:30]}...' -> {keywords}")
    assert isinstance(keywords, list) and len(keywords) <= 3, "Keyword Extractor failed"

    # Text Statistics
    stats = TextStatistics()
    metrics = stats.analyze(text)
    print(f"Text Statistics: '{text[:30]}...' -> {metrics}")
    assert metrics["word_count"] > 0, "Text Statistics word count failed"

def test_agent_integration():
    print("\n--- Running Agent Integration Tests ---")
    agent = Agent()
    
    # Process queries
    r1 = agent.process("Calculate (12 + 5) * 2")
    print(f"Response: {r1}")
    assert r1 == 34, "Agent calculator flow failed"

    r2 = agent.process("Extract keywords from the following text: Deep learning models use neural networks.")
    print(f"Response: {r2}")
    assert isinstance(r2, list), "Agent keyword extraction flow failed"

    r3 = agent.process("Analyze this text and show its statistics.")
    print(f"Response: {r3}")
    assert "word_count" in r3, "Agent statistics flow failed"

    # Test Memory
    history = agent.process("history")
    print(f"History: {history}")
    assert len(history) == 3, "Agent memory flow failed"

if __name__ == "__main__":
    print("Starting Week 8 Agentic AI System Tests...")
    test_validator()
    test_router()
    test_tools()
    test_agent_integration()
    print("\nAll tests completed successfully!")