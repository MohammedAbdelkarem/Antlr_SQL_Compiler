from expression.core import ASTNode
from expression.ddl.DataTypeNode import DataTypeNode


class ColumnDefNode(ASTNode):
    def __init__(self, name: str, type_node: "DataTypeNode", constraints=None):
        self.name = name
        self.type = type_node
        self.constraints = constraints or []  # list of constraint strings

    def add_constraint(self, constraint: str):
        if constraint:
            self.constraints.append(constraint)

    def pretty_print(self, indent: str = "") -> str:
        lines = [
            f"{indent}ColumnDef:",
            f"{indent}  Name: {self.name}",
            self.type.pretty_print(indent + '  ')
        ]
        if self.constraints:
            for constraint in self.constraints:
                lines.append(f"{indent}  Constraint: {constraint}")
        return "\n".join(lines)
