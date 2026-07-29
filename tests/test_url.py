from docscrub.cleaners.url import remove_urls


def test_remove_urls_removes_http_links():
    text = "Visit https://example.com for details"

    result = remove_urls(text)

    assert result == "Visit  for details"
