# Create a program that prints all unique elements in an array.
# Sample array: 2 3 2 5 8 1 9 8
# Sample result: 3 5 1 9

numbers = [2, 3, 2, 5, 8, 1, 9, 8]
unique_elements = []

for number in numbers:
    if numbers.count(number) == 1:
        unique_elements.append(number)

print("Array:", *numbers)
print("Unique elements:", *unique_elements)