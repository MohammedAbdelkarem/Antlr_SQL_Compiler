from expression.core import ExpressionNode


class NullLiteralNode(ExpressionNode):
    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}NullLiteral: NULL"
