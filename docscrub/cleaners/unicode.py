"""Unicode helpers for DocScrub."""

import unicodedata

import ftfy


def fix_unicode(text: str) -> str:
    """Fix broken encoding and normalize Unicode text."""

    fixed_text = ftfy.fix_text(text)
    return unicodedata.normalize("NFC", fixed_text)
