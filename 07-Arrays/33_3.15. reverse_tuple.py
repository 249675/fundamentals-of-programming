# Write a program that prints the tuple (10, 20, 30, 40, 50)
# in reverse order.

numbers = (10, 20, 30, 40, 50)
reversed_numbers = numbers[::-1]

print("Tuple: ", end="")
print(*numbers, sep=",")
print("Reverse order: ", end="")
print(*reversed_numbers, sep=",")