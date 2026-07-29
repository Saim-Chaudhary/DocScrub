from docscrub.cleaners.duplicate import remove_duplicate_lines


def test_remove_duplicate_lines_keeps_the_first_copy():
    text = "Hello\nHello\nWorld"

    result = remove_duplicate_lines(text)

    assert result == "Hello\nWorld"


def test_remove_duplicate_lines_keeps_unique_lines_in_order():
    text = "Alpha\nBeta\nAlpha\nGamma"

    result = remove_duplicate_lines(text)

    assert result == "Alpha\nBeta\nGamma"
