from expression.core import ASTNode


class AssignmentNode(ASTNode):
    def __init__(self, column_name: str, value):
        self.column_name = column_name
        self.value = value   # ExpressionNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}Assignment:\n"
            f"{indent}  Column: {self.column_name}\n"
            f"{self.value.pretty_print(indent + '  ')}"
        )
