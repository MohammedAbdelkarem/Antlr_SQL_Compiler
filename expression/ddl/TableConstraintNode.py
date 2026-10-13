from expression.core import ASTNode


class TableConstraintNode(ASTNode):
    def __init__(self, name: str | None, definition: ASTNode):
        self.name = name
        self.definition = definition

    def pretty_print(self, indent: str = "") -> str:
        name_str = self.name if self.name is not None else "(none)"
        return (
            f"{indent}TableConstraint:\n"
            f"{indent}  Name: {name_str}\n"
            f"{self.definition.pretty_print(indent + '  ')}"
        )
