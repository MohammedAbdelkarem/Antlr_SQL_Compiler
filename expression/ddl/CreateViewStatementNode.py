
from expression.core import ASTNode
from expression.core import StatementNode


class CreateViewStatementNode(StatementNode):
    def __init__(self, name: str, select: ASTNode):
        self.name = name
        self.select = select

    def pretty_print(self, indent: str = "") -> str:
        return (
            f"{indent}CreateView:\n"
            f"{indent}  Name: {self.name}\n"
            f"{self.select.pretty_print(indent + '  ')}"
        )
