# Define a function rand_elem(array) that returns a randomly selected
# array element. Use the function to print a few random elements.

import random


def rand_elem(array):
    return random.choice(array) # Losujemy jeden element z listy i go zwracamy.


numbers = [3, 7, 11, 15, 20]

for draw in range(5): # Wykonujemy pętlę pięć razy. Zmienna draw przyjmuje wartości od 0 do 4.
    print(rand_elem(numbers)) # Losujemy jedną liczbę i wyświetlamy ją w osobnym wierszu.