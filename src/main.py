from generate import generate_page
from copy_content import copy


def main():
    copy()
    generate_page("./content/index.md", "./template.html", "./public")


main()
