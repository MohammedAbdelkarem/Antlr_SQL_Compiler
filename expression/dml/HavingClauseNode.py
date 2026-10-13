from expression.core import ASTNode


class HavingClauseNode(ASTNode):
    def __init__(self, condition):
        self.condition = condition   # ExpressionNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}Having:\n"
            f"{self.condition.pretty_print(indent + '  ')}"
        )
