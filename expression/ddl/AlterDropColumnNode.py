from expression.core import ASTNode


class AlterDropColumnNode(ASTNode):
    def __init__(self, column_name: str):
        self.column_name = column_name

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}AlterDropColumn: {self.column_name}"
