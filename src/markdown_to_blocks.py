def markdown_to_blocks(markdown):
    new_blocks = []

    for line in markdown.split("\n\n"):
        current_line = line.strip()
        if current_line != "":
            new_blocks.append(current_line)
    return new_blocks
