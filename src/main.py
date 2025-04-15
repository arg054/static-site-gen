from generate import generate_page, get_dir, generate_pages
from copy_content import copy


def main():
    copy()
    generate_pages(get_dir("./content"), "./content", "./template.html", "./public")


main()
