from expression.core import ASTNode


class AlterRenameTableNode(ASTNode):
    def __init__(self, new_name: str):
        self.new_name = new_name

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}AlterRenameTable: {self.new_name}"
