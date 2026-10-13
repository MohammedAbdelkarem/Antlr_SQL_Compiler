
from expression.core import ASTNode


class DataTypeNode(ASTNode):
    def __init__(self, type_name: str):
        self.type = type_name

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}DataType: {self.type}"
