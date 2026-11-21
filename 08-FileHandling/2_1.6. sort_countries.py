#The following program prints a list of countries from 'countries.txt' file. Modify the program to print a list #of #countries sorted alphabetically.
###
# Reads the entire contents of a file
#
def read_from_file(name):  # Funkcja przyjmuje nazwę pliku.
    with open(name, "r") as file:  # Otwieramy plik do odczytu.
        content = file.read()  # Wczytujemy całą zawartość jako jeden tekst.
    return content  # Zwracamy odczytany tekst.


file_content = read_from_file("countries.txt")  # Wczytujemy dane krajów.
file_lines = file_content.splitlines()  # Dzielimy tekst na listę wierszy.
file_lines = sorted(file_lines)  # Tworzymy posortowaną listę i zapisujemy ją w file_lines.

for line in file_lines:  # Pobieramy kolejne wiersze w kolejności alfabetycznej.
    print(line)  # Wypisujemy każdy kraj w osobnym wierszu.