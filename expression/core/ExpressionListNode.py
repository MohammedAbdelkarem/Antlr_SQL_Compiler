from expression.core.ASTNode import ASTNode
from expression.core.ExpressionNode import ExpressionNode


class ExpressionListNode(ASTNode):
    def __init__(self):
        self.expressions: list[ExpressionNode] = []

    def add_expression(self, expr: "ExpressionNode"):
        if expr is not None:
            self.expressions.append(expr)

    def pretty_print(self, indent: str = "") -> str:
        lines = [f"{indent}ExpressionList:"]
        for expr in self.expressions:
            lines.append(expr.pretty_print(indent + "  "))
        return "\n".join(lines)
