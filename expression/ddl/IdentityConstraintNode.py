
from expression.core import ASTNode


class IdentityConstraintNode(ASTNode):
    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}IdentityConstraint"
