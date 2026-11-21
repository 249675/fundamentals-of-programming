# Create a dictionary that describes your favorite book or movie with at least five key-value pairs. 
# Then, create a program that writes the dictionary data to the favourite.json file.

import json

# Tworzymy słownik z informacjami o filmie.
favourite = {"title": "Inception", "director": "Christopher Nolan",
             "year": 2010, "genre": "Science fiction", "duration_minutes": 148}

# Tryb "w" tworzy plik lub nadpisuje jego dotychczasową zawartość.
# Kodowanie UTF-8 pozwala zapisywać m.in. polskie litery.

with open("favourite.json", "w", encoding="utf-8") as file:
    # dump() zamienia słownik na format JSON i zapisuje go do pliku.
    # ensure_ascii=False zapisuje np. „ł” jako „ł”.
    # indent=4 ustawia wcięcia na cztery spacje na każdym poziomie.
    json.dump(favourite, file, ensure_ascii=False, indent=4)

# Po wyjściu z bloku with plik jest już zamknięty.
print("Data has been written to favourite.json.")  # Wyświetlamy potwierdzenie w konsoli.