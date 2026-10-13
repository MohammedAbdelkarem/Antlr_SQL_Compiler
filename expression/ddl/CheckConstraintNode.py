from expression.core import ASTNode
from expression.core import ExpressionNode


class CheckConstraintNode(ASTNode):
    def __init__(self, condition: "ExpressionNode"):
        self.condition = condition

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}Check:\n{self.condition.pretty_print(indent + '  ')}"
