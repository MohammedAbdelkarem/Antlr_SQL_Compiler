from expression.core import ASTNode


class FromClauseNode(ASTNode):
    def __init__(self, source: ASTNode):
        self.source = source

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}From:\n"
            f"{self.source.pretty_print(indent + '  ')}"
        )
