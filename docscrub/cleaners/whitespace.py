import re


def remove_extra_whitespace(text: str) -> str:
    """
    Remove unnecessary spaces and new lines.
    """

    # replace multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    # replace multiple new lines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()