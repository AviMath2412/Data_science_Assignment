import ast
import operator
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}
class Calculator:
    def evaluate(self, expression: str):
        """
        Evaluate a mathematical expression safely.
        """
        try:
            node = ast.parse(expression, mode="eval").body
            return self._evaluate_node(node)

        except Exception as e:
            return f"Calculation Error: {e}"
    def _evaluate_node(self, node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            return OPERATORS[type(node.op)](
                self._evaluate_node(node.left),
                self._evaluate_node(node.right),
            )
        elif isinstance(node, ast.UnaryOp):
            return OPERATORS[type(node.op)](
                self._evaluate_node(node.operand)
            )
        raise TypeError("Unsupported Expression")