# An array contains integer numbers: 2, 6, 4, 9, 7.
# Create a program that prints the array values graphically using asterisks.
# Define a function star(n) that returns the given number of asterisks
# as a string. Use the function in the program.

def star(n):
    return "*" * n


numbers = [2, 6, 4, 9, 7]

for number in numbers:
    print(f"{number}: {star(number)}")