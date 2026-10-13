from expression.core import ASTNode
from expression.ddl.ColumnDefNode import ColumnDefNode


class AlterAddColumnNode(ASTNode):
    def __init__(self, column: "ColumnDefNode"):
        self.column = column

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}AlterAddColumn:\n{self.column.pretty_print(indent + '  ')}"
