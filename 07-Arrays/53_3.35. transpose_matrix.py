# Create a function transpose_matrix(m) that returns the transpose of m.
# Print the transposed matrices below in rows and columns.

def transpose_matrix(m):
    transposed = []

    for column_index in range(len(m[0])):
        new_row = []
        for row in m:
            new_row.append(row[column_index])
        transposed.append(new_row)

    return transposed


matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]],
]

for matrix in matrices:
    for row in transpose_matrix(matrix):
        print(*row)
    print()