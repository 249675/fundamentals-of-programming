#The file dogs.json contains data about dogs. Write a program that prints information about dogs younger than 5 years.

import json  # Importujemy moduł do odczytu danych w formacie JSON.

with open("dogs.json", encoding="utf-8") as file:  # Otwieramy plik do odczytu.
    dogs = json.load(file)  # Wczytujemy listę słowników. Każdy słownik opisuje jednego psa.

for dog in dogs:  # W każdym obrocie pobieramy słownik jednego psa.
    if dog["age"] < 5:  # Pobieramy wiek psa i sprawdzamy, czy ma mniej niż 5 lat.
        for key, value in dog.items():  # Pobieramy nazwę pola i jego wartość.
            print(f"{key}: {value}")  # Wypisujemy jedną informację o psie.
        print()  # Po wypisaniu wszystkich danych tego psa dodajemy pusty wiersz.