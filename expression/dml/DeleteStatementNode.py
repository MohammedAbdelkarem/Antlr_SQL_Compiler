from expression.core import StatementNode, ASTNode
from expression.core.ASTNode import ASTNode


class DeleteStatementNode(StatementNode):
    def __init__(self, table_source: ASTNode, where: ASTNode | None):
        self.table_source = table_source
        self.where = where

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}DeleteStatement:"]
        lines.append(self.table_source.pretty_print(indent + "  "))

        if self.where is not None:
            lines.append(self.where.pretty_print(indent + "  "))

        return "\n".join(lines)
