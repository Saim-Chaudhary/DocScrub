from docscrub import Cleaner


def test_remove_extra_whitespace():

    text = """
    Hello       World


    Test
    """

    cleaner = Cleaner()

    result = cleaner.clean(text)

    assert result == "Hello World\nTest"