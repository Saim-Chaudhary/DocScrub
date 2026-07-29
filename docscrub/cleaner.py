"""Public Cleaner class for DocScrub."""

from docscrub.cleaners.duplicate import (
    remove_duplicate_lines as remove_duplicate_lines_text,
)
from docscrub.cleaners.email import remove_emails as remove_emails_text
from docscrub.cleaners.page import remove_page_numbers as remove_page_numbers_text
from docscrub.cleaners.unicode import fix_unicode as fix_unicode_text
from docscrub.cleaners.url import remove_urls as remove_urls_text
from docscrub.cleaners.whitespace import remove_extra_whitespace
from docscrub.config import CleanerConfig


class Cleaner:
    """Run a simple sequence of text cleaners."""

    def __init__(
        self,
        fix_unicode: bool = True,
        remove_urls: bool = True,
        remove_emails: bool = True,
        remove_page_numbers: bool = True,
        remove_duplicate_lines: bool = True,
        remove_whitespace: bool = True,
    ):
        self.config = CleanerConfig(
            fix_unicode=fix_unicode,
            remove_urls=remove_urls,
            remove_emails=remove_emails,
            remove_page_numbers=remove_page_numbers,
            remove_duplicate_lines=remove_duplicate_lines,
            remove_whitespace=remove_whitespace,
        )

        self.cleaners = []

        if self.config.fix_unicode:
            self.cleaners.append(fix_unicode_text)

        if self.config.remove_urls:
            self.cleaners.append(remove_urls_text)

        if self.config.remove_emails:
            self.cleaners.append(remove_emails_text)

        if self.config.remove_page_numbers:
            self.cleaners.append(remove_page_numbers_text)

        if self.config.remove_duplicate_lines:
            self.cleaners.append(remove_duplicate_lines_text)

        if self.config.remove_whitespace:
            self.cleaners.append(remove_extra_whitespace)

    def clean(self, text: str) -> str:
        """Run text through every enabled cleaner."""

        for cleaner in self.cleaners:
            text = cleaner(text)

        return text
