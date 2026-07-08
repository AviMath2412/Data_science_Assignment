"""
Validator Module
Validates user queries before routing.
"""
class Validator:
    def validate(self, query: str):
        if not isinstance(query, str):
            return False, "Query must be a string."
        query = query.strip()
        if len(query) == 0:
            return False, "Query cannot be empty."
        if len(query) < 3:
            return False, "Query is too short."
        return True, "Validation Passed"