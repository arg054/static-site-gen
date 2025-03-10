import unittest

from leaflnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_href(self):
        node = LeafNode("a", "link", None, {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">link</a>')
