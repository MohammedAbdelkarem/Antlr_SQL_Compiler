from expression.core import ASTNode


class TableSourceNode(ASTNode):
    def __init__(self, simple_source):
        self.simple_source = simple_source      # ASTNode
        self.joins = []                         # list[ASTNode]

    def add_join(self, join):
        self.joins.append(join)

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}TableSource:"]
        lines.append(self.simple_source.pretty_print(indent + "  "))

        for join in self.joins:
            lines.append(join.pretty_print(indent + "  "))

        return "\n".join(lines).strip()
