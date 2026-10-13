from expression.core.ASTNode import ASTNode


class StatementNode(ASTNode):
    """Base class for all SQL statement AST nodes.

    This class intentionally contains no fields or methods.
    It exists to categorize all statement nodes under a common parent.
    """
    pass
