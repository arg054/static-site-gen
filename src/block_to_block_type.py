from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(text_block):
    if re.search(r"^#{1,6} ", text_block):
        return BlockType.HEADING
    if check_code(text_block):
        return BlockType.CODE
    if check_quotes(text_block):
        return BlockType.QUOTE
    if check_unordered_list(text_block):
        return BlockType.UNORDERED_LIST
    if check_ordered_list(text_block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def check_code(text_block):
    if text_block.startswith("```") and text_block.endswith("```"):
        return True
    return False


def check_quotes(text_block):
    for line in text_block.splitlines():
        if not line.startswith(">"):
            return False

    return True


def check_unordered_list(text_block):
    for line in text_block.splitlines():
        if not line.startswith("- "):
            return False
    return True


def check_ordered_list(text_block):
    count = 1
    for line in text_block.splitlines():
        if not line.startswith(f"{count}. "):
            return False
        count += 1
    return True
