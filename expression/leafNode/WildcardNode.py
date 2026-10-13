from expression.core import ExpressionNode


class WildcardNode(ExpressionNode):
    def pretty_print(self, indent: str = "") -> str:
        return f"{indent}Wildcard: *"
