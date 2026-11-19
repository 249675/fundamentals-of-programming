# Define a function rand_elem(array) that returns a randomly selected
# array element. Use the function to print a few random elements.

import random


def rand_elem(array):
    return random.choice(array)


numbers = [3, 7, 11, 15, 20]

for draw in range(5):
    print(rand_elem(numbers))