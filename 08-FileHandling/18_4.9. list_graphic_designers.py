#Convenient processing of CSV documents is possible using the CSV module. Find on the Internet how to use this module. 
# Then write a program that, based on the it_company.csv file, prints the first name, last name and email 
# (in the given order, without Job Title) of people employed in the position of 'Graphic Designer'. Sample result:

#GRAPHIC DESIGNERS
#=================
#Chris Martin,chris.martin@example.com
#Jane Taylor,jane.taylor@example.com
#...
#...

import csv  # Importujemy moduł do odczytywania plików CSV.

print("GRAPHIC DESIGNERS")
print("=================")

# Otwieramy plik do odczytu. newline="" zostawia obsługę końców wierszy modułowi csv.
with open("it_company.csv", newline="") as file:
    for employee in csv.DictReader(file): # Odczytujemy dane każdego pracownika jako słownik.
        if employee["Job Title"] == "Graphic Designer": # Sprawdzamy dokładną nazwę stanowiska.
            # Wypisujemy imię, nazwisko i e-mail w kolejności z polecenia.
            print(f"{employee['First Name']} {employee['Last Name']},{employee['Email']}")
