from expression.core import ASTNode
from expression.core import ColumnNameListNode


class PrimaryKeyConstraintNode(ASTNode):
    def __init__(self, columns: "ColumnNameListNode"):
        self.columns = columns

    def pretty_print(self, indent: str = "") -> str:
        return (
            f"{indent}PrimaryKey:\n"
            f"{self.columns.pretty_print(indent + '  ')}"
        )
