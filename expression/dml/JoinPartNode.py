from expression.core import ASTNode


class JoinPartNode(ASTNode):
    def __init__(self, join_type, table, condition):
        self.join_type = join_type      # ASTNode
        self.table = table              # ASTNode
        self.condition = condition      # ASTNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}JoinPart:\n"
            f"{self.join_type.pretty_print(indent + '  ')}\n"
            f"{self.table.pretty_print(indent + '  ')}\n"
            f"{self.condition.pretty_print(indent + '  ')}"
        )
