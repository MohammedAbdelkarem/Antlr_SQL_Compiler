from expression.core.StatementNode import StatementNode
from expression.core.ASTNode import ASTNode


class SelectStatementNode(StatementNode):
    def __init__(self):
        self.distinct = False
        self.top = None
        self.select_items = []     # list[ASTNode]
        self.into = None
        self.from_ = None          # "from" is a keyword in Python
        self.where = None
        self.group_by = None
        self.having = None
        self.order_by = None
        self.offset_fetch = None

    def set_distinct(self, distinct: bool):
        self.distinct = distinct

    def set_top(self, top: ASTNode):
        self.top = top

    def add_select_item(self, item: ASTNode):
        if item is not None:
            self.select_items.append(item)

    def set_into(self, into: ASTNode):
        self.into = into

    def set_from(self, from_node: ASTNode):
        self.from_ = from_node

    def set_where(self, where: ASTNode):
        self.where = where

    def set_group_by(self, group_by: ASTNode):
        self.group_by = group_by

    def set_having(self, having: ASTNode):
        self.having = having

    def set_order_by(self, order_by: ASTNode):
        self.order_by = order_by

    def set_offset_fetch(self, offset_fetch: ASTNode):
        self.offset_fetch = offset_fetch

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}SelectStatement:"]

        if self.distinct:
            lines.append(f"{indent}  DISTINCT")

        if self.top is not None:
            lines.append(self.top.pretty_print(indent + "  "))

        lines.append(f"{indent}  SelectItems:")
        for item in self.select_items:
            lines.append(item.pretty_print(indent + "    "))

        if self.into is not None:
            lines.append(self.into.pretty_print(indent + "  "))

        if self.from_ is not None:
            lines.append(self.from_.pretty_print(indent + "  "))

        if self.where is not None:
            lines.append(self.where.pretty_print(indent + "  "))

        if self.group_by is not None:
            lines.append(self.group_by.pretty_print(indent + "  "))

        if self.having is not None:
            lines.append(self.having.pretty_print(indent + "  "))

        if self.order_by is not None:
            lines.append(self.order_by.pretty_print(indent + "  "))

        if self.offset_fetch is not None:
            lines.append(self.offset_fetch.pretty_print(indent + "  "))

        return "\n".join(lines).strip()
