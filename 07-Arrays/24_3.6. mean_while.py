# An array contains values: 15, 8, 31, 47, 2, 19.
# Create a program that calculates and prints the array and the arithmetic
# mean of array values. Use the while loop statement.

numbers = [15, 8, 31, 47, 2, 19]
total = 0
index = 0

while index < len(numbers):
    total += numbers[index]
    index += 1

mean = total / len(numbers)

print("Array:", end=" ")  # Wyświetlamy etykietę i zostajemy w tym samym wierszu.
for number in numbers:
    print(number, end=" ")  # Wyświetlamy kolejną liczbę i spację.
print()  # Po wypisaniu całej listy przechodzimy do nowego wiersza.

print("Arithmetic mean:", mean)  # Wyświetlamy obliczoną średnią.