from markdown_to_html_node import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            line = line.removeprefix("# ")
            return line

    raise Exception("Can't detect a header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_file(from_path)
    title = extract_title(markdown)
    template = read_file(template_path)
    markdown = markdown_to_html_node(markdown).to_html()
    pass


def read_file(file, placeholder=None, content=None):
    content = None
    with open(file, "r") as file:
        if placeholder and content:
            # replace conent here, generate new html
            pass
        else:
            content = file.read()
    return content
