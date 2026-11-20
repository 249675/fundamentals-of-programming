# Write a program that checks whether the first array is a subset
# of the second one, meaning all elements of the first array appear
# in the second array.

array1 = [2, 5, 7] # Lista elementów, których szukamy.
array2 = [1, 2, 4, 5, 7, 9]  # Lista, w której ich szukamy.
is_subset = True  # Na początku zakładamy, że wszystkie elementy się znajdą.

for number in array1: # Pobieramy po kolei każdą liczbę z pierwszej listy.
    if number not in array2: # Sprawdzamy, czy tej liczby brakuje w drugiej liście.
        is_subset = False # Brak choć jednej liczby wystarczy, żeby wynik był False.
        break # Od razu kończymy pętlę, bo wynik jest już znany.

print("First array:", array1)  # Wyświetlamy pierwszą listę z nawiasami i przecinkami.
print("Second array:", array2)  # Tak samo wyświetlamy drugą listę.
print("Is the first array a subset of the second?", is_subset)  # Wyświetlamy wynik sprawdzenia.