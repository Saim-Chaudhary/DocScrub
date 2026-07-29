from docscrub.cleaners.page import remove_page_numbers


def test_remove_page_numbers_removes_page_label_lines():
    text = "Intro\nPage 5\nEnd"

    result = remove_page_numbers(text)

    assert result == "Intro\n\nEnd"


def test_remove_page_numbers_does_not_remove_normal_numbers_in_sentences():
    text = "There are 12 apples."

    result = remove_page_numbers(text)

    assert result == "There are 12 apples."
