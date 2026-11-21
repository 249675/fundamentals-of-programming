#A traffic camera records passing vehicles. The camera saves their registration numbers in the file vehicle.txt.
#  Write a program that calculates and prints how many registered cars come from each province of Poland. 
# The list of provinces and the corresponding first letters of the vehicle registration numbers are contained in the file province.csv.

#Hint: use the dictionary containing the letters corresponding to the provinces and the numbers of 
# vehicles whose first letters of the registration number match the letters of the province.

import csv  # Importujemy moduł do odczytu plików CSV.

provinces = {}  # Pod każdą literą zapiszemy nazwę województwa.
counts = {}  # Pod każdą literą zapiszemy liczbę rejestracji.

# utf-8-sig pozwala odczytać polskie znaki.
# newline="" zostawia obsługę końców wierszy modułowi csv.

with open("province.csv", encoding="utf-8-sig", newline="") as file:
    for row in csv.DictReader(file):  # Każdy wiersz danych odczytujemy jako słownik.
        letter = row["Letter"]  # Pobieramy literę z kolumny Letter.
        provinces[letter] = row["Name"]  # Pod tą literą zapisujemy nazwę województwa.
        counts[letter] = 0  # Ustawiamy licznik tego województwa na zero.

with open("vehicle.txt", encoding="utf-8-sig") as file:
    for line in file:  # Czytamy po jednej rejestracji z każdego wiersza.
        plate = line.strip().upper()  # Usuwamy białe znaki z brzegów i zamieniamy litery na wielkie.
        if plate and plate[0] in counts:  # Sprawdzamy, czy wpis jest niepusty i czy znamy jego pierwszą literę.
            counts[plate[0]] += 1  # Zwiększamy licznik przypisany do pierwszej litery rejestracji.

for letter, province in provinces.items():  # Pobieramy literę i nazwę każdego województwa.
    print(f"{province}: {counts[letter]}")  # Używamy tej samej litery do pobrania wyniku z counts.

    #Ta sama litera łączy oba słowniki. Dla rejestracji KMH7218 zapis plate[0] daje "K". Program zwiększa counts["K"] o 1, a przy wypisywaniu wyniku bierze nazwę "Małopolskie" z provinces["K"].
