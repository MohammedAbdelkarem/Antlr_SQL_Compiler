from expression.core import ASTNode


class AssignmentListNode(ASTNode):
    def __init__(self):
        self.assignments = []   # list of AssignmentNode

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}Assignments:"]
        for assignment in self.assignments:
            lines.append(assignment.pretty_print(indent + "  "))
        return "\n".join(lines).strip()
