from expression.core import ExpressionNode


class LiteralNode(ExpressionNode):
    def __init__(self, value: str):
        self.value = value

    def pretty_print(self, indent: str) -> str:
        return f"{indent}Literal: {self.value}"
