import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.keyword_extractor import KeywordExtractor
from tools.calculator import Calculator
calc = Calculator()
print(calc.evaluate("12+5"))
print(calc.evaluate("5*8"))
print(calc.evaluate("(10+5)*3"))
print(calc.evaluate("100/4"))
print(calc.evaluate("2**5"))
extractor = KeywordExtractor()
sample_text = """
Agentic AI systems use tools, memory, reasoning,
and planning to solve complex problems efficiently.
"""
print("\nKeywords:")
print(extractor.extract(sample_text))