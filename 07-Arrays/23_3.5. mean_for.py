# An array contains values: 15, 8, 31, 47, 2, 19.
# Create a program that calculates and prints the array and the arithmetic
# mean of array values. Use the for loop statement.

numbers = [15, 8, 31, 47, 2, 19]
total = 0

for number in numbers:
    total += number

mean = total / len(numbers)

print("Array:", end=" ")  # Wyświetlamy etykietę i zostajemy w tym samym wierszu.
for number in numbers:
    print(number, end=" ")  # Wyświetlamy liczbę i po niej spację.
print()  # Po wypisaniu wszystkich liczb przechodzimy do nowego wiersza.

print("Arithmetic mean:", mean)  # Wyświetlamy obliczoną średnią.