#Write a program to record voting. Voting results are saved in the voting.json file with the structure below. The program takes a person's name from the keyboard and increases the number of votes for that person by 1. If this is a new person, they are added to the list with a vote count of 1. You can run the program multiple times to add additional votes to the json file.

import json  # Importujemy moduł do odczytu i zapisu danych w formacie JSON.

file_name = "voting.json"  # Ustalamy nazwę pliku z wynikami głosowania.

try:  # Próbujemy wczytać dotychczasowe wyniki.
    with open(file_name, encoding="utf-8") as file:
        votes = json.load(file)  # Wczytujemy zapisane głosy jako słownik.
except FileNotFoundError:  # Jeśli pliku jeszcze nie ma, zaczynamy od pustego słownika.
    votes = {}

# Pobieramy imię i usuwamy białe znaki z początku i końca wpisu.
person_name = input("Name of the person you are voting for: ").strip()

if person_name:  # Zapisujemy głos tylko wtedy, gdy wpis zawiera tekst.
    if person_name in votes:  # Sprawdzamy, czy imię jest już kluczem w słowniku.
        votes[person_name] += 1  # Doliczamy głos do dotychczasowego wyniku tej osoby.
    else:
        votes[person_name] = 1  # Dodajemy nową osobę z jednym głosem.

    with open(file_name, "w", encoding="utf-8") as file:  # Tworzymy plik lub nadpisujemy go aktualnymi wynikami.
        # Zapisujemy cały słownik. Zachowujemy polskie znaki i stosujemy wcięcia po 4 spacje.
        json.dump(votes, file, ensure_ascii=False, indent=4)

    print(f"{person_name}: {votes[person_name]}")  # Wyświetlamy imię i aktualną liczbę głosów.
else:
    print("No vote recorded. Enter a name.")  # Informujemy, że pusty wpis nie został zapisany.
