from expression.core import ASTNode
from expression.core import ExpressionNode


class DefaultConstraintNode(ASTNode):
    def __init__(self, value: "ExpressionNode"):
        self.value = value

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}Default:\n{self.value.pretty_print(indent + '  ')}"
