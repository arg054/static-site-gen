import unittest

from generate import extract_title


class TestExtractTitle(unittest.TestCase):
    def test1(self):
        line_test = "This is a line\n# This is a header!\nThis is another line"
        heading = extract_title(line_test)
        self.assertEqual(heading, "This is a header!")

    def test2(self):
        line_test = (
            "This is a line\n       # This is a header!     \nThis is another line"
        )
        heading = extract_title(line_test)
        self.assertEqual(heading, "This is a header!")

    def test_error(self):
        self.assertRaises(Exception)
