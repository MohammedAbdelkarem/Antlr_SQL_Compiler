from expression.core import ExpressionNode


class StringLiteralNode(ExpressionNode):
    def __init__(self, value: str):
        self.value = value

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}StringLiteral: '{self.value}'"
