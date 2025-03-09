import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "paragraph test")
        node2 = HTMLNode("p", "paragraph test")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode(
            "ol", "", [HTMLNode("li", "Iteml 1"), HTMLNode("li", "Iteml 2")]
        )
        node2 = HTMLNode(
            "ol", "", [HTMLNode("li", "Iteml 1"), HTMLNode("li", "Iteml 2")]
        )
        self.assertEqual(node, node2)

    def test_eq(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "link", None, {"href": "https://duckduckgo.com/"})
        self.assertNotEqual(node, node2)

    if __name__ == "__main__":
        unittest.main()
