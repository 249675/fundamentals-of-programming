#Write a program that calculates the number of vowels in the text entered from the keyboard. Use regular expressions.


import re # Importujemy moduł do wyszukiwania tekstu za pomocą wyrażeń regularnych.

text = input("Enter text: ")

vowels = re.findall(r"[aeiouyąęó]", text, re.IGNORECASE)
# Szukamy wszystkich samogłosek wymienionych w nawiasach kwadratowych.
# re.IGNORECASE sprawia, że pasują zarówno małe, jak i wielkie litery.

print("Number of vowels:", len(vowels))
