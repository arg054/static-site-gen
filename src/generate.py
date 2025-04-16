import os
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
    title = extract_title(markdown)
    markdown = markdown_to_html_node(markdown).to_html()
    write_file(dest_path, (title, markdown, template))


def read_file(file_path):
    file = open(file_path, "r")
    return file.read()


def write_file(dest_path, content, basepath):
    output_content = (
        content[2]
        .replace("{{ Title }}", content[0])
        .replace("{{ Content }}", content[1])
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    output_file = open(f"{dest_path}/index.html", "w")
    output_file.write(output_content)
    output_file.close()


def generate_pages(files, from_path, template_path, dest_path, basepath):

    if not files:
        return

    file = files.pop(0)

    if os.path.isfile(f"{from_path}/{file}"):
        print(
            f"Generating page from {from_path}/{file} to {dest_path}/{file} using {template_path}"
        )
        markdown = read_file(f"{from_path}/{file}")
        template = read_file(template_path)
        title = extract_title(markdown)
        markdown = markdown_to_html_node(markdown).to_html()

        write_file(
            f"{dest_path}/{file}".replace("/index.md", ""),
            (title, markdown, template),
            basepath,
        )

    if os.path.isdir(f"{from_path}/{file}"):
        os.mkdir(f"{dest_path}/{file}")
        for f in os.listdir(f"{from_path}/{file}"):
            files.append(f"{file}/{f}")

    generate_pages(files, from_path, template_path, dest_path, basepath)


def get_dir(path):
    files = os.listdir(path)
    return files
