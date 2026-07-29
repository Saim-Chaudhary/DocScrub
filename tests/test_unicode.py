from docscrub.cleaners.unicode import fix_unicode


def test_fix_unicode_corrects_broken_encoding():
    text = "FranÃ§ais"

    result = fix_unicode(text)

    assert result == "Français"


def test_fix_unicode_keeps_regular_text_readable():
    text = "Hello world"

    result = fix_unicode(text)

    assert result == "Hello world"
