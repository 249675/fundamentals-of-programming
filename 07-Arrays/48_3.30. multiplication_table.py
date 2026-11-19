# An array of size 5 by 5 is filled with zeros.
# Modify its values to create a multiplication table from 1 to 5.
# Use loop statements and print the array.

table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

for row_index in range(len(table)):
    for column_index in range(len(table[row_index])):
        table[row_index][column_index] = (row_index + 1) * (column_index + 1)

for row in table:
    for value in row:
        print(f"{value:2}", end=" ")
    print()