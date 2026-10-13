from expression.core import ASTNode


class AlterDropConstraintNode(ASTNode):
    def __init__(self, constraint_name: str):
        self.constraint_name = constraint_name

    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}AlterDropConstraint: {self.constraint_name}"
