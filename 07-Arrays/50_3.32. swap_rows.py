# A two-dimensional array of size 3 by 5 contains integer numbers.
# Swap the first and last rows. Print the array in rows and columns
# before and after the change.

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [5, 4, 3, 2, 1],
]

print("Before:")
for row in array:
    print(*row)

array[0], array[-1] = array[-1], array[0]

print("After:")
for row in array:
    print(*row)