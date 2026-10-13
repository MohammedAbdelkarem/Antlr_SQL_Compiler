from expression.core import ASTNode
from expression.ddl.ColumnDefNode import ColumnDefNode


class ColumnDefListNode(ASTNode):
    def __init__(self):
        self.defs: list["ColumnDefNode"] = []

    def add_column_def(self, def_node: "ColumnDefNode"):
        self.defs.append(def_node)

    def pretty_print(self, indent: str = "") -> str:
        lines = [f"{indent}ColumnDefs:"]
        for def_node in self.defs:
            lines.append(def_node.pretty_print(indent + "  "))
        return "\n".join(lines)
