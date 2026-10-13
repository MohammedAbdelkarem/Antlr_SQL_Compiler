from expression.core import ASTNode
from expression.ddl.DataTypeNode import DataTypeNode


class AlterColumnTypeNode(ASTNode):
    def __init__(self, column_name: str, new_type: "DataTypeNode"):
        self.column_name = column_name
        self.new_type = new_type

    def pretty_print(self, indent: str = "") -> str:
        return (
            f"{indent}AlterColumnType:\n"
            f"{indent}  ColumnName: {self.column_name}\n"
            f"{self.new_type.pretty_print(indent + '  ')}"
        )
