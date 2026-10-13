from expression.core import ASTNode
from expression.ddl.TableConstraintNode import TableConstraintNode


class TableConstraintListNode(ASTNode):
    def __init__(self):
        self.constraints: list["TableConstraintNode"] = []

    def add_constraint(self, constraint: "TableConstraintNode"):
        self.constraints.append(constraint)

    def pretty_print(self, indent: str = "") -> str:
        lines = [f"{indent}TableConstraints:"]
        for c in self.constraints:
            lines.append(c.pretty_print(indent + "  "))
        return "\n".join(lines)
