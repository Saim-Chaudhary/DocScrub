"""Configuration values for DocScrub cleaners."""

from dataclasses import dataclass


@dataclass
class CleanerConfig:
    """Simple on/off switches for the cleaning pipeline."""

    fix_unicode: bool = True
    remove_urls: bool = True
    remove_emails: bool = True
    remove_page_numbers: bool = True
    remove_duplicate_lines: bool = True
    remove_whitespace: bool = True
