# Define a function compare(array1, array2) that returns True if both
# arrays are the same or False otherwise. Arrays are the same if they
# have the same length and equal values at corresponding indexes.
# Compare the four pairs below. Print both arrays and the result.

def compare(array1, array2):
    if len(array1) != len(array2): # Najpierw porównujemy liczbę elementów.
        return False

    for index in range(len(array1)):
        if array1[index] != array2[index]: # Porównujemy elementy na tej samej pozycji.
            return False

    return True # Jeśli wszystkie elementy się zgadzają, zwracamy True.


pairs = [  
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2]),
]

for array1, array2 in pairs:
    print("Array1:", end=" ")  # Wyświetlamy etykietę i zostajemy w tym samym wierszu.
    for item in array1:
        print(item, end=" ")  # Wypisujemy kolejny element pierwszej listy i spację.
    print()  # Po całej pierwszej liście przechodzimy do nowego wiersza.

    print("Array2:", end=" ")
    for item in array2:
        print(item, end=" ")  # Tak samo wypisujemy elementy drugiej listy.
    print()  # Przechodzimy do wiersza z wynikiem porównania.

    if compare(array1, array2):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are different")

    print()  # Dodajemy pusty wiersz między parami.