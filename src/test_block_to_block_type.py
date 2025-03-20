import unittest

from block_to_block_type import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        md = "###### Heading 6"
        heading = block_to_block_type(md)
        self.assertEqual(heading, BlockType.HEADING)

    def test_code(self):
        md = '```print("hello world")\nprint("also print this")```'
        code = block_to_block_type(md)
        self.assertEqual(code, BlockType.CODE)

    def test_quote(self):
        md = "> This is a quote.\n> This is another quote.\n> This is also a quote."
        quote = block_to_block_type(md)
        self.assertEqual(quote, BlockType.QUOTE)

    def test_unordered_list(self):
        md = "- This is a quote.\n- This is another quote.\n- This is also a quote."
        ul = block_to_block_type(md)
        self.assertEqual(ul, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        md = "1. This is a list item\n2. This is a list item\n3. This is a list item"
        ol = block_to_block_type(md)
        self.assertEqual(ol, BlockType.ORDERED_LIST)
