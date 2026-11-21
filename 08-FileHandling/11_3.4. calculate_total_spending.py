#A file report.txt contains an email with shopping report. Write a program that calculates the total value of #money spent.

#Hint: To open and read a text file that contains special characters (like the Euro sign €), you need to ensure #that the file is read using the correct character encoding. The most common encoding for such cases is UTF-8, #which supports a wide range of characters, including special symbols. Here is an example use of the open() #function:

import re  # Importujemy moduł do obsługi wyrażeń regularnych.

email_file = "report.txt"  # Ustalamy nazwę pliku z raportem.

with open(email_file, "r", encoding="utf-8") as file:
    email = file.read()  # Wczytujemy całą wiadomość jako jeden tekst.

pattern = r"€(\d+(?:\.\d{2})?)"  # Szukamy np. €102 lub €15.50.
amounts = re.findall(pattern, email)  # Pobieramy kwoty jako tekst, bez znaku €.

total = 0  # Zaczynamy sumowanie od zera.
for amount in amounts:
    total += float(amount)  # Zamieniamy tekst na liczbę i dodajemy do sumy.

print(f"Total spent: €{total:.2f}")  # Wyświetlamy sumę z dwoma miejscami po kropce.

# Wzorzec wyszukuje kwoty takie jak €102 i €15.50.

# 1. Prefiks r zostawia ukośniki \ w tekście wzorca do odczytania przez moduł re.
# 2. Znak € szuka symbolu euro.
# 3. \d+ szuka jednej lub więcej cyfr po znaku euro, np. 15 albo 102.
# 4. \. szuka dosłownej kropki.
# 5. \d{2} szuka dokładnie dwóch cyfr po kropce, np. 50.
# 6. (?:\.\d{2}) grupuje kropkę i dwie cyfry w jedną część.
#    Znak ? po nawiasie sprawia, że cała ta część jest opcjonalna.
#    Dlatego pasuje zarówno €15.50, jak i €102.
# 7. Zewnętrzne nawiasy (...) przechwytują samą kwotę.
#    Znak € jest poza nimi, więc findall() zwraca np. "15.50" bez symbolu euro.