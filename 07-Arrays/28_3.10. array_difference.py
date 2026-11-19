# Two arrays contain the following integer numbers:
# [4, 36, 12, 28, 9, 44, 5] and [5, 1, 36].
# Print the numbers from the first array that do not appear in the second.

array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]
difference = []

for number in array1:  # Sprawdzamy po kolei liczby z pierwszej listy.
    if number not in array2:  # Sprawdzamy, czy tej liczby nie ma na drugiej liście.
        difference = difference + [number]  # Dołączamy jednoelementową listę z tą liczbą.

print(difference)  # Wyświetlamy wynik z nawiasami i przecinkami.