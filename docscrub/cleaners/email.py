"""Email cleanup for DocScrub."""

from docscrub.patterns.regex import EMAIL_PATTERN


def remove_emails(text: str) -> str:
    """Remove email addresses from text."""

    return EMAIL_PATTERN.sub("", text)
