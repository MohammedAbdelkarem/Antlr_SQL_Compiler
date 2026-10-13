from expression.core import StatementNode


class InsertDefaultValuesStatementNode(StatementNode):
    def __init__(self, table_name: str):
        self.table_name = table_name

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}InsertDefaultValues:\n"
            f"{indent}  Table: {self.table_name}"
        )
