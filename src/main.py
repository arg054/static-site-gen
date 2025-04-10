from generate import extract_title


def main():
    line_test = "This is a line\n# This is a header!\nThis is another line".split("\n")
    print(extract_title(line_test))


main()
