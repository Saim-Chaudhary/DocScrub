"""Page number cleanup for DocScrub."""

from docscrub.patterns.regex import PAGE_NUMBER_PATTERN


def remove_page_numbers(text: str) -> str:
    """Remove common page number lines from text."""

    return PAGE_NUMBER_PATTERN.sub("", text)
