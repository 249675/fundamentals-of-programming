#The file it_company.csv contains a list of employees. Write a program that displays only employees with the #position "Software Engineer". Number the items on the printed list.

file_name = "it_company.csv"  # W szablonie jest .txt, ale plik z danymi ma rozszerzenie .csv.
job_title = "Software Engineer"
number = 1

with open(file_name) as file:
    for line in file:  # Czytamy plik wiersz po wierszu.
        if job_title in line:  # Szukamy frazy w całym wierszu.
            print(f"{number}. {line.rstrip()}")
            number += 1  # Numerujemy tylko wypisane wiersze.