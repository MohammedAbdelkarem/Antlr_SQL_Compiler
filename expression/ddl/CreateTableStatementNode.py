from expression.core import StatementNode
from expression.ddl.ColumnDefListNode import ColumnDefListNode
from expression.ddl.TableConstraintListNode import TableConstraintListNode


class CreateTableStatementNode(StatementNode):
    def __init__(self, table_name: str, columns: "ColumnDefListNode", constraints: "TableConstraintListNode | None"):
        self.table_name = table_name
        self.columns = columns
        self.constraints = constraints

    def pretty_print(self, indent: str = "") -> str:
        lines = [
            f"{indent}CreateTable:",
            f"{indent}  Table: {self.table_name}",
            self.columns.pretty_print(indent + "  ")
        ]

        if self.constraints is not None:
            lines.append(self.constraints.pretty_print(indent + "  "))

        return "\n".join(lines)
