from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from html_node import HTMLNode
from text_to_html import (
    text_node_to_html_block,
)


def markdown_to_html_node(markdown):
    nodes = []

    for block in markdown_to_blocks(markdown):
        block_type = block_to_block_type(block)
        nodes.append(text_node_to_html_block(block_type, block))

    return HTMLNode("div", None, nodes)
