from text_node import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT)
    new_nodes = [initial_node]
    node_def = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}

    for markdown_def, node_type in node_def.items():
        new_nodes = split_nodes_delimiter(new_nodes, markdown_def, node_type)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes
