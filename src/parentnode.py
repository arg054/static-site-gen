from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None or children is None:
            raise ValueError("Tag and children cannot be None")
        if not isinstance(children, list):
            raise ValueError("Children nodes must be in a list")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        child_nodes = ""
        for ch in self.children:
            child_nodes += ch.to_html()
        return f"<{self.tag}>{child_nodes}</{self.tag}>"
