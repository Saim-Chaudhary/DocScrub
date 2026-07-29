# DocScrub

DocScrub is a lightweight Python library for cleaning raw text before NLP, LLM, and RAG workflows.

## Features

- Unicode fixing
- URL removal
- Email removal
- Page number removal
- Duplicate line removal
- Whitespace cleanup

## Installation

```bash
pip install docscrub
```

## Quick Start

```python
from docscrub import Cleaner

cleaner = Cleaner()

raw_text = "FranÃ§ais https://example.com user@example.com\n\nHello\nHello"
clean_text = cleaner.clean(raw_text)

print(clean_text)
```

## Examples

Input:

```text
Visit https://example.com for details
```

Output:

```text
Visit for details
```

Input:

```text
Hello
Hello
World
```

Output:

```text
Hello
World
```

## Supported Cleaners

### Unicode Cleaner

Fixes broken text encoding and normalizes Unicode characters. DocScrub uses `ftfy` for this step.

### URL Cleaner

Removes common URLs such as `https://example.com`.

### Email Cleaner

Removes email addresses such as `user@example.com`.

### Page Number Cleaner

Removes page-number-only lines such as `Page 1 of 10`, `Page 5`, or `12`.

### Duplicate Line Cleaner

Removes repeated lines while keeping the first copy.

### Whitespace Cleaner

Removes extra spaces, tabs, blank lines, and line padding.

## Project Structure

- `docscrub/` contains the library code.
- `docscrub/cleaners/` contains one simple function per cleaning step.
- `docscrub/patterns/` stores regular expression patterns shared by cleaners.
- `docscrub/utils/` is available for small helper functions.
- `tests/` contains beginner-friendly pytest tests.
- `examples/` contains short example scripts.

## Development Setup

Install the project dependencies with uv, then run the test and lint commands:

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format .
```

## Contributing

Beginner-friendly contributions are welcome.

1. Clone the repository.
2. Install the dependencies with `uv sync`.
3. Run `uv run pytest` before and after your change.
4. Keep the code simple and easy to read.
5. Open a pull request with a short description of what changed.

## License

DocScrub is released under the MIT License. See the [LICENSE](LICENSE) file for details.