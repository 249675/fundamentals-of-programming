# Write a program that prints the tuple (10, 20, 30, 40, 50)
# in reverse order.

numbers = (10, 20, 30, 40, 50)
reversed_numbers = numbers[::-1]  # Pobieramy elementy krotki od końca.

print("Tuple: ", end="")
for index in range(len(numbers)):
    if index > 0:  # Przed drugim i każdym kolejnym elementem wypisujemy przecinek.
        print(",", end="")
    print(numbers[index], end="")  # Wypisujemy liczbę i zostajemy w tym samym wierszu.
print()  # Przechodzimy do nowego wiersza.

print("Reverse order: ", end="")
for index in range(len(reversed_numbers)):
    if index > 0:
        print(",", end="")
    print(reversed_numbers[index], end="")
print()