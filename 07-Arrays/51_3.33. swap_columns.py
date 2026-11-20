# A two-dimensional array of size 3 by 5 contains integer numbers.
# Swap the first and last columns. Print the array in rows and columns
# before and after the change.

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [5, 4, 3, 2, 1],
]

print("Before:")  # Wyświetlamy tablicę przed zamianą.
for row in array:  # Pobieramy po kolei każdy wiersz.
    for number in row:  # Pobieramy kolejne liczby z bieżącego wiersza.
        print(number, end=" ")  # Wypisujemy liczbę i spację w tym samym wierszu.
    print()  # Po wypisaniu całego wiersza przechodzimy do następnej linii.

for row in array:  # Zamianę wykonujemy osobno w każdym wierszu.
    row[0], row[-1] = row[-1], row[0]  # Zamieniamy pierwszą i ostatnią liczbę miejscami.

print("After:")  # Wyświetlamy tablicę po zamianie.
for row in array:
    for number in row:
        print(number, end=" ")
    print()