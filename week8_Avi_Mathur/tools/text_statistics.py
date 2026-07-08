"""
Text Statistics Tool
Provides basic statistics about a given text.
"""
import re
class TextStatistics:
    def analyze(self, text: str):
        words = re.findall(r"\b\w+\b", text)
        sentences = re.split(r"[.!?]+", text)
        sentences = [s for s in sentences if s.strip()]
        return {
            "word_count": len(words),
            "sentence_count": len(sentences),
            "character_count": len(text)
        }