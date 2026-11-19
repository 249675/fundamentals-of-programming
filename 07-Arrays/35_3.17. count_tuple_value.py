# Write a program that counts the number of occurrences of any value
# from a tuple. Sample tuple: (50, 20, 40, 50, 30, 50).
# Sample value: 50. Number of occurrences: 3.

numbers = (50, 20, 40, 50, 30, 50)

print("Tuple: ", end="")
print(*numbers, sep=",")

value = int(input("Value: "))
print("Number of occurrences:", numbers.count(value))