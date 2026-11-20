# Define a function create_2d_arr(x, y) that returns a two-dimensional
# array filled with zeros. Then create and print a 3 by 5 array.

def create_2d_arr(x, y):  # Tworzymy tablicę z x wierszami i y kolumnami.
    array = []  # Zaczynamy od pustej listy wierszy.

    for row_index in range(x):  # Tworzymy jeden wiersz w każdym obrocie.
        row = [0] * y  # Tworzymy wiersz z y zerami.
        array = array + [row]  # Dołączamy cały wiersz jako jeden element.

    return array  # Zwracamy gotową tablicę.


array = create_2d_arr(3, 5)

for row in array:  # Pobieramy po kolei każdy wiersz.
    for number in row:  # Pobieramy kolejne liczby z tego wiersza.
        print(number, end=" ")  # Wypisujemy liczbę i spację.
    print()  # Po wypisaniu całego wiersza przechodzimy do nowej linii.

    #W pierwszym obrocie row to [0, 0, 0, 0, 0], a [row] to [[0, 0, 0, 0, 0]]. Ta dodatkowa para nawiasów sprawia, że array + [row] dodaje jeden wiersz.