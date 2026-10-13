import os
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"
from antlr4 import *
from SqlLexer import SqlLexer
from SqlParser import SqlParser
from graphviz import Digraph

def draw_tree(node, graph, parent_id=None):
    node_id = str(id(node))

    label = node.__class__.__name__

    if node.getChildCount() == 0:
        label = f"'{node.getText()}'"

    graph.node(node_id, label)

    if parent_id:
        graph.edge(parent_id, node_id)

    for i in range(node.getChildCount()):
        draw_tree(node.getChild(i), graph, node_id)


def generate_parse_tree(input_file, output_image="parse_tree.png"):
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = SqlLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SqlParser(tokens)

    tree = parser.sql_script()

    graph = Digraph(format="png")
    graph.attr(rankdir="TB")  # Top to Bottom
    draw_tree(tree, graph)
    graph.render(output_image, cleanup=True)

    print(f"Parse tree saved as {output_image}")


generate_parse_tree("input.sql", "sql_tree")