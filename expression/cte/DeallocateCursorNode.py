from expression.core import StatementNode


class DeallocateCursorNode(StatementNode):
    def __init__(self, name: str):
        self.name = name

    def pretty_print(self, indent: str) -> str:
        return f"{indent}DeallocateCursor: {self.name}"
