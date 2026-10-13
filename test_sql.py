from antlr4 import FileStream, CommonTokenStream
from SqlLexer import SqlLexer
from SqlParser import SqlParser
from expression.core import ASTBuilderVisitor
from expression.core.ASTNode import ASTNode


def main():
    stream = FileStream("input.sql", encoding="utf-8")
    lexer = SqlLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = SqlParser(tokens)

    tree = parser.sql_script()

    print("\n=== PARSE TREE (TEXT) ===\n")
    print(tree.toStringTree(recog=parser))

    # Build AST
    visitor = ASTBuilderVisitor()
    ast = visitor.visit(tree)

    print("\n=== ABSTRACT SYNTAX TREE ===\n")
    print(ast.pretty_print(""))

    # # Report semantic errors
    # if hasattr(visitor, "semantics_errors") and visitor.semantics_errors:
    #     print("\nSemantic Errors:")
    #     for error in visitor.semantics_errors:
    #         print(" -", error)
    # else:
    #     print("\nNo semantic errors.")


if __name__ == "__main__":
    main()
