from expression.core import ExpressionNode


class FunctionCallNode(ExpressionNode):
    def __init__(self, function_name: str, arguments):
        self.function_name = function_name          # str
        self.arguments = arguments                  # ExpressionListNode

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}FunctionCall: {self.function_name}"]
        if self.arguments:
            lines.append(f"{indent}  Arguments:")
            # Handle both list and ExpressionListNode
            args = self.arguments.expressions if hasattr(self.arguments, 'expressions') else self.arguments
            for arg in args:
                lines.append(arg.pretty_print(indent + "    "))
        return "\n".join(lines)
