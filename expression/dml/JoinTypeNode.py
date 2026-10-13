from expression.core import ASTNode


class JoinTypeNode(ASTNode):
    def __init__(self, join_type: str):
        self.join_type = join_type

    def pretty_print(self, indent: str) -> str:
        return f"{indent}JoinType: {self.join_type}"
