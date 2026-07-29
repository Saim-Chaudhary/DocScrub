from docscrub import Cleaner


def test_cleaner_runs_the_full_default_pipeline():
    text = (
        "FranÃ§ais https://example.com user@example.com\n"
        "Page 1 of 10\n"
        "Hello\n"
        "Hello\n"
        "   Test    line   "
    )

    cleaner = Cleaner()

    result = cleaner.clean(text)

    assert result == "Français\nHello\nTest line"


def test_cleaner_can_disable_url_removal():
    text = "Visit https://example.com"

    cleaner = Cleaner(remove_urls=False)

    result = cleaner.clean(text)

    assert "https://example.com" in result
