from expression.core import ASTNode
from expression.core import StatementNode


class AlterTableStatementNode(StatementNode):
    def __init__(self, table_name: str, action: ASTNode):
        self.table_name = table_name
        self.action = action

    def pretty_print(self, indent: str = "") -> str:
        return (
            f"{indent}AlterTable:\n"
            f"{indent}  Table: {self.table_name}\n"
            f"{self.action.pretty_print(indent + '  ')}"
        )
