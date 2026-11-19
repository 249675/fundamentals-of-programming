# A matrix is a rectangular array of values arranged in rows and columns.
# Create a function identity_matrix(n) that returns an identity matrix
# of size n. Create a second function that prints a 2D array in rows
# and columns. Print identity matrices of sizes 3, 5 and 8.

def identity_matrix(n):
    matrix = []

    for row_index in range(n):
        row = [0] * n
        row[row_index] = 1
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


for size in (3, 5, 8):
    print_matrix(identity_matrix(size))
    print()