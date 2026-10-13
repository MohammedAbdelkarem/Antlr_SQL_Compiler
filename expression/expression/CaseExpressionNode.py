from expression.core import ExpressionNode


class CaseExpressionNode(ExpressionNode):
    def __init__(self):
        self.branches = []      # list[WhenThenNode]
        self.else_expr = None   # ExpressionNode or None

    def add_branch(self, branch):
        self.branches.append(branch)

    def set_else(self, else_expr):
        self.else_expr = else_expr

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}CASE:"]

        for branch in self.branches:
            lines.append(branch.pretty_print(indent + "  "))

        if self.else_expr is not None:
            lines.append(f"{indent}  ELSE:")
            lines.append(self.else_expr.pretty_print(indent + "    "))

        return "\n".join(lines).trim() if hasattr(str, "trim") else "\n".join(lines).strip()
