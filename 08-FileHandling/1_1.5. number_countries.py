#Modify the program print_countries.py so that the printed list of countries is numbered. Sample result:

#1. Poland, Warsaw, 38265000
#2. Germany, Berlin, 83240000
#3. France, Paris, 67850000
#4. Japan, Tokyo, 125800000
#5. Canada, Ottawa, 38250000

with open("countries.txt") as file:
    countries = file.read().splitlines()  # Odczytujemy cały tekst i dzielimy go na listę wierszy.

# Po wyjściu z bloku with Python automatycznie zamyka plik.
number = 1
for country in countries:
    print(f"{number}. {country}")  # Wypisujemy numer i dane kraju.
    number += 1
