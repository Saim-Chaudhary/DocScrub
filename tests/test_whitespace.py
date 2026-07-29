from docscrub.cleaners.whitespace import remove_extra_whitespace


def test_remove_extra_whitespace_collapses_spaces_and_blank_lines():
    text = "Hello       World\n\n\nTest"

    result = remove_extra_whitespace(text)

    assert result == "Hello World\nTest"


def test_remove_extra_whitespace_removes_tabs_and_line_padding():
    text = "\t  Hello\tWorld  \n  Test  "

    result = remove_extra_whitespace(text)

    assert result == "Hello World\nTest"
