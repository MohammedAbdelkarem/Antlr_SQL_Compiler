from expression.expression.BinaryExpressionNode import BinaryExpressionNode


class SubtractExpressionNode(BinaryExpressionNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def operator(self) -> str:
        return "Subtract"
