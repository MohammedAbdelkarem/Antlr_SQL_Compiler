from expression.core import ExpressionNode


class SubqueryExpressionNode(ExpressionNode):
    def __init__(self, select):
        self.select = select    # StatementNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}Subquery:\n"
            f"{self.select.pretty_print(indent + '  ')}"
        )
