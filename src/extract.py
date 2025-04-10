def extract_title(markdown):
    with open(markdown, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("# "):
                line = line.removeprefix("# ")
                return line

    raise Exception("Can't detect a header")
