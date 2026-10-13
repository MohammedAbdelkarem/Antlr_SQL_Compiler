from expression.expression.BinaryExpressionNode import BinaryExpressionNode


class AndExpressionNode(BinaryExpressionNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def operator(self) -> str:
        return "AND"
