from expression.core.ASTNode import ASTNode


class ColumnNameListNode(ASTNode):
    def __init__(self):
        self.column_names: list[str] = []

    def add_column_name(self, name: str):
        if name is not None:
            self.column_names.append(name)

    def pretty_print(self, indent: str = "") -> str:
        lines = [f"{indent}ColumnNameList:"]
        for name in self.column_names:
            lines.append(f"{indent}  Column: {name}")
        return "\n".join(lines)
