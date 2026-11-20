# Create a program that prints all unique elements in an array.
# Sample array: 2 3 2 5 8 1 9 8
# Sample result: 3 5 1 9

numbers = [2, 3, 2, 5, 8, 1, 9, 8]
unique_elements = []

for number in numbers:
    if numbers.count(number) == 1:  # Sprawdzamy, czy liczba występuje dokładnie raz.
        unique_elements = unique_elements + [number]  # Dołączamy listę z tą jedną liczbą.

print("Array:", end=" ")  # Wypisujemy etykietę i zostajemy w tym samym wierszu.
for number in numbers:
    print(number, end=" ")  # Po każdej liczbie wypisujemy spację.
print()  # Po całej liście przechodzimy do nowego wiersza.

print("Unique elements:", end=" ")
for number in unique_elements:
    print(number, end=" ")
print()  # Kończymy drugi wiersz.