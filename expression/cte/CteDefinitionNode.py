from expression.core import ASTNode


class CteDefinitionNode(ASTNode):
    def __init__(self, name: str, columns, query):
        self.name = name
        self.columns = columns      # ColumnNameListNode or None
        self.query = query          # StatementNode

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}CteDefinition:"]
        lines.append(f"{indent}  Name: {self.name}")

        if self.columns is not None:
            lines.append(self.columns.pretty_print(indent + "  "))

        lines.append(self.query.pretty_print(indent + "  "))

        return "\n".join(lines)
