#The cities.json file contains data about selected cities in Poland. Open the json file in an editor and review its contents. Notice that the file contains an array of dictionaries.

#Then, write a program that prints information about cities.

#Note: using the encoding='utf-8' parameter when opening the file is necessary because the json file also contains Polish characters in city names that must be processed correctly. Remember to always use this parameter when opening files that contain characters other than those in the Latin alphabet.

import json  # Importujemy moduł do odczytu danych w formacie JSON.

# Otwieramy plik do odczytu. UTF-8 pozwala poprawnie odczytać nazwy takie jak „Łódź”.
with open("cities.json", encoding="utf-8") as file:
    cities = json.load(file)  # Wczytujemy dane jako listę słowników.

for city in cities:  # Zewnętrzna pętla pobiera po kolei słownik każdego miasta.
    for key, value in city.items():  # Wewnętrzna pętla pobiera klucz i jego wartość.
        print(f"{key}: {value}")  # Wypisujemy jedną informację o mieście.
    print()  # Po wypisaniu wszystkich informacji o mieście dodajemy pusty wiersz.

    
#Tutaj cities to lista słowników. 
# Pierwsza pętla wybiera miasto, a druga wypisuje jego dane. 
# Dlatego .items() wywołujemy na city.