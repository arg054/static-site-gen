from leaf_node import LeafNode
from text_node import TextNode, TextType
from html_node import HTMLNode
from block_to_block_type import BlockType
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid type")


def text_node_to_html_block(block_type, block_node):
    match block_type:
        case BlockType.PARAGRAPH:
            return HTMLNode("p", None, block_to_leaf_nodes(block_node))
        case BlockType.HEADING:
            heading_parts = block_node.split(" ", 1)
            level = heading_parts[0].count("#")
            content = heading_parts[1]
            children = block_to_leaf_nodes(content)
            return HTMLNode(f"h{level}", None, children)
        case BlockType.CODE:
            code_content = block_node.removeprefix("```\n").removesuffix("```")
            code_node = LeafNode("code", code_content)
            return HTMLNode("pre", None, [code_node])
        case BlockType.QUOTE:
            content = block_node.replace("> ", "")
            children = block_to_leaf_nodes(content)
            return HTMLNode("blockquote", None, children)
        case BlockType.UNORDERED_LIST:
            return HTMLNode(
                "ul", None, block_to_node_with_children(block_type, block_node)
            )
        case BlockType.ORDERED_LIST:
            return HTMLNode(
                "ol", None, block_to_node_with_children(block_type, block_node)
            )
        case _:
            raise Exception("Invalid type")


def block_to_node_with_children(block_type, block_node):
    child_list = []

    for node in block_node.splitlines():
        child_list.append(block_to_list_node(node, block_type))

    return child_list


def block_to_list_node(block_node, block_type):
    if block_type == BlockType.UNORDERED_LIST:
        children = block_to_leaf_nodes(block_node.split(" ", 1)[1])
        return HTMLNode("li", None, children)
    elif block_type == BlockType.ORDERED_LIST:
        children = block_to_leaf_nodes(block_node.split(". ", 1)[1])
        return HTMLNode("li", None, children)

    raise Exception("List type not recognized")


def block_to_leaf_nodes(block_node):
    paragraph_text = " ".join(block_node.splitlines())
    nodes = [TextNode(paragraph_text, TextType.TEXT)]

    for text_type, delimiter in [
        (TextType.BOLD, "**"),
        (TextType.ITALIC, "_"),
        (TextType.CODE, "`"),
    ]:
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return [text_node_to_html_node(node) for node in nodes]
