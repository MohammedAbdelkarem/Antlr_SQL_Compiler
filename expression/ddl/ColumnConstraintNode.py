from expression.core import ASTNode


class ColumnConstraintNode(ASTNode):
    def __init__(self, constraint: str):
        self.constraint = constraint

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}ColumnConstraint: {self.constraint}"
