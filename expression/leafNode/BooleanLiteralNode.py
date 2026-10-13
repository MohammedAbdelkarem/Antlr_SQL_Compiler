from expression.core import ExpressionNode


class BooleanLiteralNode(ExpressionNode):
    def __init__(self, value: bool):
        self.value = value

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}BooleanLiteral: {self.value}"
