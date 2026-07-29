"""Duplicate line cleanup for DocScrub."""


def remove_duplicate_lines(text: str) -> str:
    """Remove repeated non-empty lines while keeping the first copy."""

    seen_lines = set()
    cleaned_lines = []

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if line == "":
            cleaned_lines.append("")
            continue

        if line in seen_lines:
            continue

        seen_lines.add(line)
        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)
