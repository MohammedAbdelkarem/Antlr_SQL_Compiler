from expression.core import ExpressionNode


class ColumnReferenceNode(ExpressionNode):
    def __init__(self, column_name: str):
        self.column_name = column_name

    def pretty_print(self, indent: str) -> str:
        return f"{indent}ColumnReference: {self.column_name}"
