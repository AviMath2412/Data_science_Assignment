"""
Output Verifier
Ensures the tool execution was successful and returned a valid format.
"""

class Verifier:
    def verify(self, tool_output) -> tuple[bool, str]:
        # Check if the output is empty or None
        if tool_output is None or tool_output == "":
            return False, "Verification Failed: Tool returned empty output."
        
        # Check for specific error strings from the calculator or other tools
        if isinstance(tool_output, str) and "Error" in tool_output:
            return False, f"Verification Failed: {tool_output}"
            
        return True, "Success"