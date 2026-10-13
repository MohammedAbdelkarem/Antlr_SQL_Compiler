from expression.core import ASTNode


class AlterRenameColumnNode(ASTNode):
    def __init__(self, old_name: str, new_name: str):
        self.old_name = old_name
        self.new_name = new_name

    def pretty_print(self, indent: str = "") -> str:
        return (
            f"{indent}AlterRenameColumn:\n"
            f"{indent}  From: {self.old_name}\n"
            f"{indent}  To: {self.new_name}"
        )
