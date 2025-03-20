import unittest

from text_node import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a url", TextType.LINK, None)
        node2 = TextNode("This is a url", TextType.LINK)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a url", TextType.BOLD)
        node2 = TextNode("This is a url", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    if __name__ == "__main__":
        unittest.main()
