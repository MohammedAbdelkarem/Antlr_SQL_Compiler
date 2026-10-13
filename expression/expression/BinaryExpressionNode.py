from expression.core import ExpressionNode


class BinaryExpressionNode(ExpressionNode):
    def __init__(self, left, right):
        self.left = left      # ExpressionNode
        self.right = right    # ExpressionNode

    def operator(self) -> str:
        raise NotImplementedError("Subclasses must implement operator()")

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}{self.operator()}:\n"
            f"{self.left.pretty_print(indent + '  ')}\n"
            f"{self.right.pretty_print(indent + '  ')}"
        )
