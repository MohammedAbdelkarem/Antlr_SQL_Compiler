from expression.core import ASTNode


class SimpleTableSourceNode(ASTNode):
    def __init__(self, table_name: str, alias: str | None):
        self.table_name = table_name
        self.alias = alias

    def pretty_print(self, indent: str) -> str:
        out = f"{indent}SimpleTableSource: {self.table_name}"
        if self.alias is not None:
            out += f" AS {self.alias}"
        return out
