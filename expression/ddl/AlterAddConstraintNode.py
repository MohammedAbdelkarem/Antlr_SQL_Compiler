from expression.core import ASTNode
from expression.ddl.TableConstraintNode import TableConstraintNode


class AlterAddConstraintNode(ASTNode):
    def __init__(self, constraint: "TableConstraintNode"):
        self.constraint = constraint

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}AlterAddConstraint:\n{self.constraint.pretty_print(indent + '  ')}"
