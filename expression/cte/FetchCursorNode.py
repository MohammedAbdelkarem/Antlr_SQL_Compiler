from expression.core import StatementNode


class FetchCursorNode(StatementNode):
    def __init__(self, cursor_name: str, into_columns):
        self.cursor_name = cursor_name
        self.into_columns = into_columns   # ColumnNameListNode

    def pretty_print(self, indent: str) -> str:
        return (
            f"{indent}FetchCursor:\n"
            f"{indent}  Cursor: {self.cursor_name}\n"
            f"{self.into_columns.pretty_print(indent + '  ')}"
        )
