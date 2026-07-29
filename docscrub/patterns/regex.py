"""Regular expression patterns used by DocScrub cleaners."""

import re

URL_PATTERN = re.compile(r"https?://\S+|www\.\S+")

EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

PAGE_NUMBER_PATTERN = re.compile(
    r"^\s*(?:Page\s+\d+(?:\s+of\s+\d+)?|\d+)\s*$",
    flags=re.IGNORECASE | re.MULTILINE,
)
