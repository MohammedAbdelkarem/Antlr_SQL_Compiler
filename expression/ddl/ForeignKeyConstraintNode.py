
from expression.core import ASTNode
from expression.core import ColumnNameListNode


class ForeignKeyConstraintNode(ASTNode):
    def __init__(self, columns: "ColumnNameListNode", ref_table: str):
        self.columns = columns
        self.ref_table = ref_table

    def pretty_print(self, indent: str = "") -> str:
        return (
            f"{indent}ForeignKey:\n"
            f"{self.columns.pretty_print(indent + '  ')}\n"
            f"{indent}  References: {self.ref_table}"
        )
