from expression.core import StatementNode


class CteStatementNode(StatementNode):
    def __init__(self, main_query):
        self.definitions = []       # list of CteDefinitionNode
        self.main_query = main_query

    def add_definition(self, definition):
        self.definitions.append(definition)

    def pretty_print(self, indent: str) -> str:
        lines = [f"{indent}CTE:"]

        for definition in self.definitions:
            lines.append(definition.pretty_print(indent + "  "))

        lines.append(f"{indent}MainQuery:")
        lines.append(self.main_query.pretty_print(indent + "  "))

        return "\n".join(lines)
