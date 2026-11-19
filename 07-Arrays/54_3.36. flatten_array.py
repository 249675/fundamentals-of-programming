# Create a function that converts a two-dimensional array into a
# one-dimensional array. Print the result for each of the three arrays.

def flatten_array(array):
    flattened = []

    for row in array:
        for value in row:
            flattened.append(value)

    return flattened


arrays = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]],
]

for array in arrays:
    print(flatten_array(array))