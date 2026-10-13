from expression.core import ASTNode


class SelectStarNode(ASTNode):
    def pretty_print(self, indent: str) -> str:
        return f"{indent}SelectStar: *"
