#The computer.json file contains sample computer data. Open the json file in an editor and review its contents. Notice that the file contains a single dictionary of data.

#Then, write a program that prints information about a computer.

import json  # Importujemy moduł do obsługi formatu JSON.

# Otwieramy plik do odczytu. UTF-8 pozwala poprawnie odczytać m.in. polskie znaki.
with open("computer.json", encoding="utf-8") as file:
    computer = json.load(file)  # Odczytujemy dane z pliku jako słownik Pythona.

for key, value in computer.items():  # Pobieramy po kolei nazwę cechy i jej wartość.
    print(f"{key}: {value}")  # Wypisujemy każdą parę w osobnym wierszu.
