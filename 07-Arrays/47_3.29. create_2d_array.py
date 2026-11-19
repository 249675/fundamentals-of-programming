# Define a function create_2d_arr(x, y) that returns a two-dimensional
# array filled with zeros. Then create and print a 3 by 5 array.

def create_2d_arr(x, y):
    array = []

    for row_index in range(x):
        array.append([0] * y)

    return array


array = create_2d_arr(3, 5)

for row in array:
    print(*row)