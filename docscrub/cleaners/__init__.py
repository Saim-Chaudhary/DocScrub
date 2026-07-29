"""Cleaner functions used by DocScrub."""

from .duplicate import remove_duplicate_lines
from .email import remove_emails
from .page import remove_page_numbers
from .unicode import fix_unicode
from .url import remove_urls
from .whitespace import remove_extra_whitespace

__all__ = [
    "fix_unicode",
    "remove_duplicate_lines",
    "remove_emails",
    "remove_extra_whitespace",
    "remove_page_numbers",
    "remove_urls",
]
