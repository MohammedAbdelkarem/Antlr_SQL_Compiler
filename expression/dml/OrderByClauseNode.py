from expression.core import ASTNode


class OrderByClauseNode(ASTNode):
    def __init__(self):
        self.orders = []   # list of ASTNode

    def add_order(self, order):
        self.orders.append(order)

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}OrderBy:"]
        for order in self.orders:
            lines.append(order.pretty_print(indent + "  "))
        return "\n".join(lines).strip()
