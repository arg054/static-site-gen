from markdown_to_html_node import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            line = line.removeprefix("# ")
            return line

    raise Exception("h1 header not found.")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_file(from_path)
    template = read_file(template_path)
    markdown = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    write_file(dest_path, (title, markdown, template))


def read_file(file_path):
    file = open(file_path, "r")
    return file.read()


def write_file(dest_path, content):
    """
    content is a tuple of title, content, template
    read the template
    replace title and content
    write to dest_path
    """

    output_content = (
        content[2]
        .replace("{{ Title }}", content[0])
        .replace("{{ Content }}", content[1])
    )

    output_file = open(dest_path, "w")
    output_file.write(output_content)
    output_file.close()
