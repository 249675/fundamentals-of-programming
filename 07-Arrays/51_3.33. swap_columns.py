# A two-dimensional array of size 3 by 5 contains integer numbers.
# Swap the first and last columns. Print the array in rows and columns
# before and after the change.

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [5, 4, 3, 2, 1],
]

print("Before:")
for row in array:
    print(*row)

for row in array:
    row[0], row[-1] = row[-1], row[0]

print("After:")
for row in array:
    print(*row)