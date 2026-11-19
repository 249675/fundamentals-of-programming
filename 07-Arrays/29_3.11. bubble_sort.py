def bubblesort(array):
    result = array[:]

    for last_index in range(len(result) - 1, 0, -1):
        for index in range(last_index):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]

    return result


arrays = [
    [8, 3, 6, 1, 5],
    [12, -2, 7, 0],
    [9, 4, 4, 2, 1],
]

for array in arrays:
    print("Original:", *array)
    print("Sorted:", *bubblesort(array))