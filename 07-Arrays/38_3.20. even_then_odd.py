# Write a program to separate even and odd numbers in an array of integers.
# Put all even numbers first, and then all odd numbers.
# Sample array: [7, 9, 2, 4, 5, 6]
# Sample result: [2, 4, 6, 7, 9, 5]

numbers = [7, 9, 2, 4, 5, 6]
even_numbers = []
odd_numbers = []

print("arr =", numbers)

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

numbers = even_numbers + odd_numbers
print("arr =", numbers)