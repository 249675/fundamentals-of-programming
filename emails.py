import re


def email_sender(message):
    # Szukamy nagłówka From i pobieramy adres z nawiasów ostrych.
    match = re.search(r"^From:[^\n<]*<([^>\n]+)>", message, re.MULTILINE)
    return match.group(1) if match else ""


def email_recipient(message):
    match = re.search(r"^To:[^\n<]*<([^>\n]+)>", message, re.MULTILINE)
    return match.group(1) if match else ""


def email_subject(message):
    match = re.search(r"^Subject: *([^\n]*)", message, re.MULTILINE)
    return match.group(1) if match else ""


def email_body(message):
    # Treść zaczyna się po pierwszej pustej linii. DOTALL pozwala kropce objąć dalsze wiersze.
    match = re.search(r"\n\n(.*)", message, re.DOTALL)
    return match.group(1) if match else ""
