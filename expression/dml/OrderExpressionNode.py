from expression.core import ASTNode


class OrderExpressionNode(ASTNode):
    def __init__(self, expression, direction):
        self.expression = expression      # ExpressionNode
        self.direction = direction        # str or None

    def pretty_print(self, indent: str) -> str:
        base = (
            f"{indent}OrderExpression:\n"
            f"{self.expression.pretty_print(indent + '  ')}"
        )
        if self.direction is not None:
            base += f"\n{indent}  Direction: {self.direction}"
        return base
