from expression.core import ASTNode


class GroupByClauseNode(ASTNode):
    def __init__(self, expr_list):
        self.list = expr_list   # ExpressionListNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}GroupBy:\n"
            f"{self.list.pretty_print(indent + '  ')}"
        )
