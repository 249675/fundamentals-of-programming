# Create a program that computes the second power of each array element.
# Sample array: 8 2 5 1 9
# Sample result: 64 4 25 1 81

numbers = [8, 2, 5, 1, 9] 
squares = []  # Zaczynamy od pustej listy wyników.

for number in numbers:  # Pobieramy po kolei każdą liczbę.
    square = number ** 2  # Podnosimy bieżącą liczbę do kwadratu.
    squares = squares + [square]  # Łączymy dotychczasową listę z listą zawierającą nowy wynik.

print("Array:", end=" ")  
for number in numbers:
    print(number, end=" ") 
print()  # Po wyświetleniu wszystkich liczb przechodzimy do nowego wiersza.

print("2nd power:", end=" ")  
for square in squares:
    print(square, end=" ")  
print()  # Po wyświetleniu wszystkich wyników kończymy wiersz.