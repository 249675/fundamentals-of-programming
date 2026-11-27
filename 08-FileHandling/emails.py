#The file email.txt contains a raw email. Write a program that uses regular expressions to fetch and print:

#sender email address
#recipient email address
#email subject
#email body
#For each of the above commands, define a separate function (see below) that returns the value read from the email. Place the functions in a separate module called emails.

#email_sender()
#email_recipient()
#email_subject()
#email_body()



import re # Importujemy moduł do wyszukiwania tekstu za pomocą wzorców.


def email_sender(message):
    # Szukamy początku wiersza z napisem From:.
    # [^\n<]* pomija tekst przed znakiem <, np. imię i nazwisko.
    # ([^>\n]+) przechwytuje adres aż do znaku > lub końca wiersza.
    match = re.search(r"^From:[^\n<]*<([^>\n]+)>", message, re.MULTILINE)
    return match.group(1) if match else "" 


def email_recipient(message):
    # Działa tak samo jak email_sender, ale szukamy wiersza To:.
    match = re.search(r"^To:[^\n<]*<([^>\n]+)>", message, re.MULTILINE)
    return match.group(1) if match else ""


def email_subject(message):
    # Szukamy początku wiersza z napisem Subject:.
    # ␣* (zwykła spacja i gwiazdka) pomija spacje po dwukropku.
    # ([^\n]*) przechwytuje resztę wiersza, czyli temat wiadomości.
    match = re.search(r"^Subject: *([^\n]*)", message, re.MULTILINE)
    return match.group(1) if match else ""


def email_body(message):
    # \n\n to dwa znaki nowej linii, które tworzą pusty wiersz.
    # (.*) przechwytuje wszystko po tej przerwie.
    # Dzięki re.DOTALL kropka obejmuje też kolejne znaki nowej linii.
    match = re.search(r"\n\n(.*)", message, re.DOTALL)
    return match.group(1) if match else ""
