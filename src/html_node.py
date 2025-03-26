class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}

    def to_html(self):
        props_html = self.props_to_html()
        html = f"<{self.tag}{props_html}>"

        if self.value:
            html += self.value

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"

        return html

    def props_to_html(self):
        if not self.props:
            return ""
        output = ""
        for key, val in self.props.items():
            output += f' {key}="{val}"'
        return output

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
