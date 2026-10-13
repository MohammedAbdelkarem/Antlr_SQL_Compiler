from expression.core import StatementNode


class InsertSelectStatementNode(StatementNode):
    def __init__(self, table_name: str, columns, select):
        self.table_name = table_name
        self.columns = columns          # ColumnNameListNode or None
        self.select = select            # ASTNode

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}InsertSelect:"]
        lines.append(f"{indent}  Table: {self.table_name}")

        if self.columns is not None:
            lines.append(self.columns.pretty_print(indent + "  "))

        lines.append(self.select.pretty_print(indent + "  "))

        return "\n".join(lines)
