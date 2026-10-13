from expression.core import ASTNode


class OffsetFetchClauseNode(ASTNode):
    def __init__(self, offset, fetch):
        self.offset = offset      # ExpressionNode
        self.fetch = fetch        # ExpressionNode or None

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}OffsetFetch:"]
        lines.append(self.offset.pretty_print(indent + "  "))

        if self.fetch is not None:
            lines.append(self.fetch.pretty_print(indent + "  "))

        return "\n".join(lines)
