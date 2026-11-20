# Define a function occurs(number, array) that returns True if a given
# number is present in an array.
# Check whether the number entered from the keyboard is present
# in the array [15, 38, 7, 23, 14].

def occurs(number, array):
    return number in array  # Zwracamy True, jeśli liczba jest na liście, albo False w przeciwnym razie.


numbers = [15, 38, 7, 23, 14] # Lista, w której szukamy liczby.
number = int(input("Number: ")) # Pobieramy wpisaną wartość i zamieniamy ją na liczbę całkowitą.

print("Array:", end=" ")  # Wypisujemy etykietę i zostajemy w tym samym wierszu.
for value in numbers:
    print(value, end=" ")  # Wypisujemy kolejną liczbę i spację.
print()  # Po wypisaniu całej listy przechodzimy do nowego wiersza.

if occurs(number, numbers):  # Jeśli funkcja zwróci True, wyświetlamy informację o znalezieniu liczby.
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")  # Ten komunikat pojawia się, gdy funkcja zwróci False.