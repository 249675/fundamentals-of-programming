# A two-dimensional array of size 2 by 4 contains integer numbers.
# Create a program that prints the array values in rows and columns.

array = [
    [3, 8, 2, 5],
    [9, 1, 4, 7],
]

for row in array:  # Pobieramy po kolei każdy wiersz.
    for number in row:  # Przechodzimy po liczbach w bieżącym wierszu.
        print(number, end=" ")  # Wypisujemy liczbę i spację w tym samym wierszu.
    print()  # Po wypisaniu wszystkich liczb przechodzimy do nowego wiersza.