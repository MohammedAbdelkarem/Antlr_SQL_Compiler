from expression.core import StatementNode


class TruncateTableStatementNode(StatementNode):
    def __init__(self, table_name: str):
        self.table_name = table_name

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}TruncateTable: {self.table_name}"
