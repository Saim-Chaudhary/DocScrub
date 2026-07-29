"""URL cleanup for DocScrub."""

from docscrub.patterns.regex import URL_PATTERN


def remove_urls(text: str) -> str:
    """Remove common URL patterns from text."""

    return URL_PATTERN.sub("", text)
