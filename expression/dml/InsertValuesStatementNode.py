from expression.core import StatementNode


class InsertValuesStatementNode(StatementNode):
    def __init__(self, table_name: str, columns, values):
        self.table_name = table_name
        self.columns = columns      # ColumnNameListNode or None
        self.values = values        # ValueListNode

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}InsertValues:"]
        lines.append(f"{indent}  Table: {self.table_name}")

        if self.columns is not None:
            lines.append(self.columns.pretty_print(indent + "  "))

        lines.append(self.values.pretty_print(indent + "  "))

        return "\n".join(lines)
