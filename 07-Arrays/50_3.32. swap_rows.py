# A two-dimensional array of size 3 by 5 contains integer numbers.
# Swap the first and last rows. Print the array in rows and columns
# before and after the change.

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [5, 4, 3, 2, 1],
]

print("Before:") # Wyświetlamy tablicę przed zamianą.
for row in array:  # Pobieramy po kolei każdy wiersz.
    for number in row:  # Pobieramy kolejne liczby z bieżącego wiersza.
        print(number, end=" ")  # Wypisujemy liczbę i spację w tym samym wierszu.
    print()  # Po wypisaniu całego wiersza przechodzimy do następnej linii.

array[0], array[-1] = array[-1], array[0] # Zamieniamy pierwszy i ostatni wiersz miejscami.

print("After:") # Wyświetlamy tablicę po zamianie.
for row in array:
    for number in row:
        print(number, end=" ")
    print()