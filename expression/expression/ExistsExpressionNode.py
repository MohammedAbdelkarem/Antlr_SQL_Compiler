from expression.core import ExpressionNode


class ExistsExpressionNode(ExpressionNode):
    def __init__(self, subquery):
        self.subquery = subquery    # StatementNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}EXISTS:\n"
            f"{self.subquery.pretty_print(indent + '  ')}"
        )
