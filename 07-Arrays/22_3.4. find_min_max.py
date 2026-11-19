# An array contains numbers: -15, 8, -31, 47, -2, 19.
# Create a program that finds and prints the maximum and minimum number.
# Do not use available functions to find the maximum and minimum.

numbers = [-15, 8, -31, 47, -2, 19]
smallest = numbers[0] # Pierwszą liczbę uznajemy na start za najmniejszą znalezioną.
largest = numbers[0] # Tę samą liczbę uznajemy na start za największą znalezioną.

for number in numbers:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number

print("Maximum:", largest)
print("Minimum:", smallest)