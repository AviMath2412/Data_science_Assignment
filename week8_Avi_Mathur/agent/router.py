"""
Intent Router
Routes validated queries to the appropriate tool.
"""
import re
class Router:
    def route(self, query: str) -> str:
        query = query.lower()
        if (
            "calculate" in query
            or re.search(r"[0-9]+\s*[\+\-\*/]", query)
            or any(op in query for op in ["+", "-", "*", "/", "**"])
        ):
            return "calculator"
        if any(word in query for word in [
            "keyword",
            "keywords",
            "extract"
        ]):
            return "keywords"
        if any(word in query for word in [
            "statistics",
            "stats",
            "count",
            "analyze",
            "analysis"
        ]):
            return "statistics"
        return "general"