from expression.core.StatementNode import StatementNode
from expression.core.StatementBlockNode import StatementBlockNode


class IfStatementNode(StatementNode):
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition      # ExpressionNode - the IF condition
        self.if_block = if_block       # StatementBlockNode - the THEN block
        self.else_block = else_block   # StatementBlockNode or None - the ELSE block

    def pretty_print(self, indent: str = "") -> str:
        lines = [f"{indent}IF:"]
        
        # Print condition
        if self.condition:
            lines.append(f"{indent}  Condition:")
            lines.append(self.condition.pretty_print(indent + "    "))
        
        # Print IF block
        if self.if_block:
            lines.append(f"{indent}  THEN:")
            lines.append(self.if_block.pretty_print(indent + "    "))
        
        # Print ELSE block if exists
        if self.else_block:
            lines.append(f"{indent}  ELSE:")
            lines.append(self.else_block.pretty_print(indent + "    "))
        
        return "\n".join(lines)
