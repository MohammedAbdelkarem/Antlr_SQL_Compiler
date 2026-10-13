from expression.core import ASTNode


class TopClauseNode(ASTNode):
    def __init__(self, value, percent: bool):
        self.value = value        # ASTNode
        self.percent = percent    # bool

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}TopClause: "
            f"{self.value.pretty_print('')}"
            f"{' PERCENT' if self.percent else ''}"
        )
