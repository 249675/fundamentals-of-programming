#Write a program that saves data of employees employed in the position of 'Software Engineer' to the file #'software_engineer.txt'. Data is available in the file 'it_company.csv'.

#Hint: Read employee data line by line. For each line, check if it contains the name of the indicated position. #If so, write this line to the output file.

import csv

with open("it_company.csv", newline="") as source:
    employees = csv.DictReader(source) # Używamy nagłówków CSV jako kluczy słownika, np. "Job Title".

    with open("software_engineer.txt", "w", newline="") as target: # Otwieramy plik wynikowy do zapisu. Tryb "w" tworzy plik lub nadpisuje jego zawartość.
        writer = csv.DictWriter(target, fieldnames=employees.fieldnames) # Ustawiamy taką samą kolejność kolumn jak w pliku wejściowym.
        for employee in employees: # Pobieramy po kolei dane każdego pracownika jako słownik.
            if employee["Job Title"] == "Software Engineer": # Sprawdzamy, czy stanowisko dokładnie odpowiada szukanej nazwie.
                writer.writerow(employee)  # Zapisujemy wszystkie pola pasującego pracownika.
