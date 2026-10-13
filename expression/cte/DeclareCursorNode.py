from expression.core import StatementNode


class DeclareCursorNode(StatementNode):
    def __init__(self, name: str, select):
        self.name = name
        self.select = select   # StatementNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}DeclareCursor:\n"
            f"{indent}  Name: {self.name}\n"
            f"{self.select.pretty_print(indent + '  ')}"
        )
