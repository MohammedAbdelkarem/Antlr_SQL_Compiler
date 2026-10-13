from expression.core import ASTNode


class WhenThenNode(ASTNode):
    def __init__(self, condition, result):
        self.condition = condition    # ExpressionNode
        self.result = result          # ExpressionNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}WHEN:\n"
            f"{self.condition.pretty_print(indent + '  ')}\n"
            f"{indent}THEN:\n"
            f"{self.result.pretty_print(indent + '  ')}"
        )
