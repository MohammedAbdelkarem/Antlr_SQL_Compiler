from expression.core import StatementNode


class UseDatabaseStatementNode(StatementNode):
    def __init__(self, database_name: str):
        self.database_name = database_name

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}UseDatabase: {self.database_name}"
