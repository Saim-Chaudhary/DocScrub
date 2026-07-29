import re


def remove_extra_whitespace(text: str) -> str:
    """Remove extra spaces, tabs, and blank lines."""

    cleaned_lines = []
    for raw_line in text.splitlines():
        line = raw_line.replace("\t", " ")
        line = re.sub(r" +", " ", line).strip()

        if line == "":
            continue

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()
