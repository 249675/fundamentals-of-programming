#Create an array with 5 dictionaries, each containing a country and its population. Then, print the array contents. Sample result:

# Przykładowe, zaokrąglone dane do ćwiczenia.
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 68000000},
    {"name": "Japan", "population": 125000000},
    {"name": "Canada", "population": 39000000},
]

print(f"{'COUNTRY':<12} POPULATION") # Wypisujemy nagłówki dwóch kolumn.

for country in countries:  # W każdym obrocie pobieramy jeden słownik z listy.
    print(f"{country['name']:<12} {country['population']}")


#:<12 oznacza wyrównanie tekstu do lewej (<) w polu o szerokości co najmniej 12 znaków.