import unittest

from texttohtml import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode


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
