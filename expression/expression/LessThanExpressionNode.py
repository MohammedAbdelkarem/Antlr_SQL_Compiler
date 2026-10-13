from expression.expression.BinaryExpressionNode import BinaryExpressionNode


class LessThanExpressionNode(BinaryExpressionNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def operator(self) -> str:
        return "LessThan"
