from expression.core import StatementNode


class UpdateStatementNode(StatementNode):
    def __init__(self, table_name: str, assignments, from_node, where):
        self.table_name = table_name              # str
        self.assignments = assignments            # AssignmentListNode
        self.from_ = from_node                    # ASTNode or None
        self.where = where                        # ASTNode or None

    def pretty_print(self, indent: str) -> str:
        lines = [
            f"{indent}UpdateStatement:",
            f"{indent}  Table: {self.table_name}",
            self.assignments.pretty_print(indent + '  ')
        ]

        if self.from_ is not None:
            lines.append(self.from_.pretty_print(indent + "  "))

        if self.where is not None:
            lines.append(self.where.pretty_print(indent + "  "))

        return "\n".join(lines)
