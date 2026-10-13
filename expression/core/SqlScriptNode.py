from expression.core.ASTNode import ASTNode


class SqlScriptNode(ASTNode):
    def __init__(self):
        self.children: list[ASTNode] = []

    def add_child(self, node: ASTNode):
        if node is not None:
            self.children.append(node)

    def pretty_print(self, indent: str = "") -> str:
        lines = [f"{indent}SqlScript:"]
        for child in self.children:
            lines.append(child.pretty_print(indent + "  "))
        return "\n".join(lines)
