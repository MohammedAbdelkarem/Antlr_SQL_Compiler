from expression.expression.BinaryExpressionNode import BinaryExpressionNode


class NotEqualsExpressionNode(BinaryExpressionNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def operator(self) -> str:
        return "NotEquals"
