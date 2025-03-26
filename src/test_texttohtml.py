import unittest

from text_to_html import text_node_to_html_node, text_node_to_html_block, BlockType
from text_node import TextNode, TextType
from leaf_node import LeafNode, HTMLNode


class TestTextToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("link", TextType.LINK, "https://www.google.com")
        node2 = LeafNode("a", "link", {"href": "https://www.google.com"})
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, node2)

    def test_error(self):
        self.assertRaises(Exception)

    def test_heading1(self):
        md = "# Heading 1"
        node = HTMLNode("h1", None, [HTMLNode(None, "Heading 1")])
        self.assertEqual(text_node_to_html_block(BlockType.HEADING, md), node)

    def test_heading2(self):
        md = "###### Heading 6"
        node = HTMLNode("h6", None, [HTMLNode(None, "Heading 6")])
        self.assertEqual(text_node_to_html_block(BlockType.HEADING, md), node)

    def test_ordered_list(self):
        md = "1. Item 1\n2. Item 2\n3. Item 3"
        block = HTMLNode(
            "ol",
            None,
            [
                HTMLNode("li", None, [HTMLNode(None, "Item 1")]),
                HTMLNode("li", None, [HTMLNode(None, "Item 2")]),
                HTMLNode("li", None, [HTMLNode(None, "Item 3")]),
            ],
        )
        self.assertEqual(text_node_to_html_block(BlockType.ORDERED_LIST, md), block)

    def test_unordered_list(self):
        md = "- Item 1\n- Item 2\n- Item 3"
        block = HTMLNode(
            "ul",
            None,
            [
                HTMLNode("li", None, [HTMLNode(None, "Item 1")]),
                HTMLNode("li", None, [HTMLNode(None, "Item 2")]),
                HTMLNode("li", None, [HTMLNode(None, "Item 3")]),
            ],
        )
        self.assertEqual(text_node_to_html_block(BlockType.UNORDERED_LIST, md), block)

    def test_code_block(self):
        md = """```
This is code
```"""
        node = HTMLNode("pre", None, [HTMLNode("code", "This is code\n")])
        self.assertEqual(text_node_to_html_block(BlockType.CODE, md), node)

    def test_quote_block(self):
        md = "> This is a quote.\n> This is also a quote."
        node = HTMLNode(
            "blockquote",
            None,
            [HTMLNode(None, "This is a quote. This is also a quote.")],
        )
        self.assertEqual(text_node_to_html_block(BlockType.QUOTE, md), node)

    def test_paragraph(self):
        md = "This is a paragraph of text."
        node = HTMLNode("p", None, [LeafNode(None, "This is a paragraph of text.")])
        self.assertEqual(text_node_to_html_block(BlockType.PARAGRAPH, md), node)
