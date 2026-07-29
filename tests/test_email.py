from docscrub.cleaners.email import remove_emails


def test_remove_emails_removes_email_addresses():
    text = "Contact user@example.com today"

    result = remove_emails(text)

    assert result == "Contact  today"
