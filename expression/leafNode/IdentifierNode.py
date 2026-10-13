from expression.core import ASTNode


class IdentifierNode(ASTNode):
    def __init__(self, name: str):
        self.name = name

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}Identifier: {self.name}"
