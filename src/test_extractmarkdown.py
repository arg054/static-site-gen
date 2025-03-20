import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


class TestImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


class TestLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [google link](https://www.google.com/) and a [duckduckgo link](https://duckduckgo.com/)"
        )
        self.assertListEqual(
            [
                ("google link", "https://www.google.com/"),
                ("duckduckgo link", "https://duckduckgo.com/"),
            ],
            matches,
        )

    def test_no_links(self):
        matches = extract_markdown_links("This is a text without any links")
        self.assertListEqual(
            [],
            matches,
        )
