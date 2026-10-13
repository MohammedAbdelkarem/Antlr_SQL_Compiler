from expression.core import ExpressionNode


class InExpressionNode(ExpressionNode):
    def __init__(self, left, right):
        self.left = left      # ExpressionNode
        # ASTNode (ExpressionListNode or SubqueryExpressionNode)
        self.right = right

    def pretty_print(self, indent: str) -> str:
        lines = [
            f"{indent}IN:",
            self.left.pretty_print(indent + '  ')
        ]
        # Handle both ExpressionListNode and list
        if hasattr(self.right, 'pretty_print'):
            lines.append(self.right.pretty_print(indent + '  '))
        elif hasattr(self.right, 'expressions'):
            lines.append(f"{indent}  Values:")
            for val in self.right.expressions:
                lines.append(val.pretty_print(indent + "    "))
        elif isinstance(self.right, list):
            lines.append(f"{indent}  Values:")
            for val in self.right:
                if hasattr(val, 'pretty_print'):
                    lines.append(val.pretty_print(indent + "    "))
        return "\n".join(lines)
