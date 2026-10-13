from expression.core import StatementNode
from expression.core import ColumnNameListNode


class CreateIndexStatementNode(StatementNode):
    def __init__(self, name: str, table: str, columns: "ColumnNameListNode"):
        self.name = name
        self.table = table
        self.columns = columns

    def pretty_print(self, indent: str = "") -> str:
        return (
            f"{indent}CreateIndex:\n"
            f"{indent}  Name: {self.name}\n"
            f"{indent}  Table: {self.table}\n"
            f"{self.columns.pretty_print(indent + '  ')}"
        )
