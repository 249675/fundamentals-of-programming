# Write a program that counts the number of occurrences of any value
# from a tuple. Sample tuple: (50, 20, 40, 50, 30, 50).
# Sample value: 50. Number of occurrences: 3.

numbers = (50, 20, 40, 50, 30, 50)

print("Tuple: ", end="")  # Wypisujemy etykietę i zostajemy w tym samym wierszu.
for index in range(len(numbers)):  # Przechodzimy po indeksach krotki.
    if index > 0:
        print(",", end="")  # Wstawiamy przecinek przed każdą liczbą poza pierwszą.
    print(numbers[index], end="")  # Wypisujemy liczbę spod bieżącego indeksu.
print()  # Po wypisaniu całej krotki przechodzimy do nowego wiersza.

value = int(input("Value: "))  # Pobieramy szukaną wartość i zamieniamy ją na liczbę całkowitą.
print("Number of occurrences:", numbers.count(value))  # Liczymy, ile razy value występuje w krotce.