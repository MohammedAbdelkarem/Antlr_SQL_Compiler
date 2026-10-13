from expression.core import ASTNode


class ValueListNode(ASTNode):
    def __init__(self):
        self.rows = []   # list[ExpressionListNode]

    def add_row(self, row):
        self.rows.append(row)

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}ValueList:"]
        for row in self.rows:
            lines.append(row.pretty_print(indent + "  "))
        return "\n".join(lines).strip()
