from expression.core import ExpressionNode


class NotExpressionNode(ExpressionNode):
    def __init__(self, operand):
        self.operand = operand    # ExpressionNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}NOT:\n"
            f"{self.operand.pretty_print(indent + '  ')}"
        )
