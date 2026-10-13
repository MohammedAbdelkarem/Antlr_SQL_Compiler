from expression.core import ASTNode


class WhereClauseNode(ASTNode):
    def __init__(self, condition):
        self.condition = condition    # ExpressionNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}Where:\n"
            f"{self.condition.pretty_print(indent + '  ')}"
        )
