# Functions for calculating statistics and formatting an array of numbers.

def sort_numbers(array): # Tworzymy listę uporządkowaną rosnąco.
    ordered = [] #pusta lista

    for number in array: # Bierzemy kolejne liczby z oryginalnej listy.
        index = 0 # Za każdym razem szukamy miejsca od początku posortowanej listy.
        while index < ordered_length(ordered) and ordered[index] <= number:
            index += 1 # Mijamy liczby mniejsze od bieżącej lub jej równe.
        ordered[index:index] = [number]  # Wstawiamy liczbę na znalezionej pozycji. Zapis index:index wskazuje pusty fragment listy. Wstawienie do niego [number] dodaje liczbę przed elementem o indeksie index i przesuwa resztę w prawo. Na przykład dla ordered = [3, 7, 8], number = 5 i index = 1, zapis ordered[1:1] = [5] daje [3, 5, 7, 8].

    return ordered # Zwracamy nową, posortowaną listę.



def ordered_length(array): # Liczymy elementy listy za pomocą pętli.
    count = 0
    for number in array:
        count += 1 # Każdy element zwiększa licznik o 1.
    return count


def second_largest(array):
    return sort_numbers(array)[-2] # Po sortowaniu pobieramy przedostatni element.


def min_max(array):
    smallest = array[0] # Na start pierwsza liczba jest naszym minimum.
    largest = array[0] # Ta sama liczba jest też naszym początkowym maksimum.

    for number in array:
        if number < smallest:
            smallest = number # Zapisujemy nowe minimum.
        if number > largest:
            largest = number # Zapisujemy nowe maksimum.

    return [smallest, largest]  # Zwracamy obie wartości w jednej liście.


def difference(array):
    smallest, largest = min_max(array) # Przypisujemy dwie wartości z listy do dwóch zmiennych.
    return largest - smallest # Obliczamy różnicę między maksimum a minimum.



def median(array):
    ordered = sort_numbers(array) # Najpierw ustawiamy liczby rosnąco.
    count = ordered_length(ordered) # Liczymy elementy posortowanej listy.
    middle = count // 2 # Wyznaczamy indeks środkowej pozycji.

    if count % 2 == 1: # Przy nieparzystej liczbie elementów mamy jedną środkową wartość.
        return ordered[middle]

    return (ordered[middle - 1] + ordered[middle]) / 2  # Przy parzystej liczbie bierzemy średnią dwóch środkowych wartości.


def numbers_as_string(array):
    result = "" # Zaczynamy od pustego tekstu.

    for number in array:
        if result: # Jeśli w tekście jest już jakaś liczba, dodajemy separator.
            result += "-"
        result += f"{number}" # Zamieniamy bieżącą liczbę na tekst i ją dopisujemy.

    return result