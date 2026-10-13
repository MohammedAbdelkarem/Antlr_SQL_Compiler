from expression.core import ExpressionNode


class BetweenExpressionNode(ExpressionNode):
    def __init__(self, expr, lower, upper):
        self.expr = expr        # ExpressionNode
        self.lower = lower      # ExpressionNode
        self.upper = upper      # ExpressionNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}Between:\n"
            f"{self.expr.pretty_print(indent + '  ')}\n"
            f"{self.lower.pretty_print(indent + '  ')}\n"
            f"{self.upper.pretty_print(indent + '  ')}"
        )
