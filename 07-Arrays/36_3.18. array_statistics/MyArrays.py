# Functions for calculating statistics and formatting an array of numbers.

def sort_numbers(array):
    ordered = []

    for number in array:
        index = 0
        while index < ordered_length(ordered) and ordered[index] <= number:
            index += 1
        ordered[index:index] = [number]

    return ordered


def ordered_length(array):
    count = 0
    for number in array:
        count += 1
    return count


def second_largest(array):
    return sort_numbers(array)[-2]


def min_max(array):
    smallest = array[0]
    largest = array[0]

    for number in array:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    return [smallest, largest]


def difference(array):
    smallest, largest = min_max(array)
    return largest - smallest


def median(array):
    ordered = sort_numbers(array)
    count = ordered_length(ordered)
    middle = count // 2

    if count % 2 == 1:
        return ordered[middle]

    return (ordered[middle - 1] + ordered[middle]) / 2


def numbers_as_string(array):
    result = ""

    for number in array:
        if result:
            result += "-"
        result += f"{number}"

    return result