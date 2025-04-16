import sys
from generate import generate_page, get_dir, generate_pages
from copy_content import copy


def main():
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]
        print(f"building to docs with {basepath} ")
        copy("./static", "./docs")
        generate_pages(
            get_dir("./content"), "./content", "./template.html", "./docs", basepath
        )

    else:
        print("building to public")
        copy("./static", "./public")
        generate_pages(
            get_dir("./content"), "./content", "./template.html", "./public", "/"
        )


main()
