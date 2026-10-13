from expression.core import ASTNode


class SelectItemNode(ASTNode):
    def __init__(self, expression, alias):
        self.expression = expression    # ExpressionNode
        self.alias = alias              # str or None

    def pretty_print(self, indent: str) -> str:
        result = (
            f"{indent}SelectItem:\n"
            f"{self.expression.pretty_print(indent + '  ')}"
        )
        if self.alias is not None:
            result += f"\n{indent}  Alias: {self.alias}"
        return result
