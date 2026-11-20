# Create a function that converts a two-dimensional array into a
# one-dimensional array. Print the result for each of the three arrays.

def flatten_array(array):  # Zamieniamy listę wierszy na jedną listę liczb.
    flattened = []  # Zaczynamy od pustej listy wynikowej.

    for row in array:  # Pobieramy po kolei każdy wiersz.
        for value in row:  # Pobieramy po kolei każdą liczbę z bieżącego wiersza.
            flattened = flattened + [value]  # Dołączamy bieżącą liczbę do listy wynikowej.

    return flattened  # Zwracamy listę po przejściu przez wszystkie wiersze.


arrays = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]],
]

for array in arrays:  # Przetwarzamy każdą tablicę osobno.
    print(flatten_array(array))  # Wyświetlamy wynik z nawiasami i przecinkami.