# An array contains the integers [[-38, 19], [5, 40], [-7, 11], [29, 16]].
# Find the smallest and largest values and print the row and column
# in which each is located.

array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]
smallest = array[0][0]
largest = array[0][0]
min_row, min_column = 1, 1
max_row, max_column = 1, 1

for row_number, row in enumerate(array, start=1):
    for column_number, value in enumerate(row, start=1):
        if value < smallest:
            smallest = value
            min_row, min_column = row_number, column_number

        if value > largest:
            largest = value
            max_row, max_column = row_number, column_number

print(f"Smallest value: {smallest}, row {min_row}, column {min_column}")
print(f"Largest value: {largest}, row {max_row}, column {max_column}")