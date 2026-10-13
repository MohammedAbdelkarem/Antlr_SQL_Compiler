from expression.core.StatementNode import StatementNode


class StatementBlockNode(StatementNode):
    def __init__(self):
        self.statements: list[StatementNode] = []

    def add_statement(self, stmt: StatementNode):
        if stmt is not None:
            self.statements.append(stmt)

    def pretty_print(self, indent: str = "") -> str:
        lines = [f"{indent}StatementBlock:"]
        for stmt in self.statements:
            lines.append(stmt.pretty_print(indent + "  "))
        return "\n".join(lines)
