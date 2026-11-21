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
    # Szukamy nagłówka From i pobieramy adres z nawiasów ostrych.
    match = re.search(r"^From:[^\n<]*<([^>\n]+)>", message, re.MULTILINE)
    return match.group(1) if match else "" 


def email_recipient(message):
    # Szukamy wiersza zaczynającego się od To: i przechwytujemy adres odbiorcy.
    match = re.search(r"^To:[^\n<]*<([^>\n]+)>", message, re.MULTILINE)
    return match.group(1) if match else ""


def email_subject(message):
    # Po Subject: pomijamy spacje i przechwytujemy temat do końca wiersza.
    match = re.search(r"^Subject: *([^\n]*)", message, re.MULTILINE)
    return match.group(1) if match else ""


def email_body(message):
    # Treść zaczyna się po pierwszej pustej linii.
    # Dwa znaki \n oddzielają nagłówki od treści wiadomości.
    # DOTALL pozwala kropce dopasować również znaki nowej linii w treści.
    match = re.search(r"\n\n(.*)", message, re.DOTALL)
    return match.group(1) if match else ""

# Wzorzec szuka adresu nadawcy w wierszu takim jak:
# From: Jan Kowalski <jan.kowalski@example.com>
#
# 1. Prefiks r przekazuje zapis \n do modułu re jako część wzorca.
#    W samym wyrażeniu regularnym \n oznacza znak nowej linii.
# 2. ^From: szuka tekstu „From:” na początku wiersza.
#    re.MULTILINE sprawia, że ^ działa na początku każdego wiersza wiadomości.
# 3. [^\n<]* dopasowuje zero lub więcej znaków innych niż \n i <.
#    W przykładzie ten fragment obejmuje spację, imię, nazwisko i kolejną spację.
# 4. < dopasowuje znak otwierający przed adresem.
# 5. ([^>\n]+) przechwytuje adres. Znak + wymaga co najmniej jednego znaku,
#    a [^>\n] pozwala czytać dalej aż do > lub końca wiersza.
# 6. > dopasowuje znak zamykający po adresie.
# 7. Jeśli znaleziono dopasowanie, match.group(1) zwraca tekst z nawiasów (),
#    czyli „jan.kowalski@example.com”. Przy braku dopasowania match to None.
#
# Używamy zwykłego * po [^\n<]. Zapis \* szukałby dosłownej gwiazdki.