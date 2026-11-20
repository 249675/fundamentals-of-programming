#Create a program that sorts elements of an array containing integer numbers. Apply the Bubble Sort sorting algorithm. Define a function bubblesort(array) that returns the sorted array. Try to sort and print any three arrays.



def bubblesort(array):
    result = array[:] # Kopiujemy całą listę. Zamiany wykonujemy na kopii.

    for last_index in range(len(result) - 1, 0, -1): # Po każdym przebiegu skracamy sprawdzany fragment o jeden element., zaczynamy od końca, dlatego -1, 0 - kończymy, skok o 1 w dół.
        for index in range(last_index):   # Wybieramy indeks lewego elementu z każdej pary sąsiadów.
            if result[index] > result[index + 1]: # Sprawdzamy, czy lewa liczba jest większa od prawej.
                result[index], result[index + 1] = result[index + 1], result[index] # Zamieniamy liczby miejscami.

    return result # Zwracamy posortowaną kopię.


arrays = [
    [8, 3, 6, 1, 5],
    [12, -2, 7, 0],
    [9, 4, 4, 2, 1],
]

for array in arrays: # Pobieramy po kolei każdą listę.
    print("Original:", array)  # Wyświetlamy oryginalną listę z nawiasami i przecinkami.
    print("Sorted:", bubblesort(array))  # Wyświetlamy posortowaną kopię.