#An expression contains operators for adding and subtracting single-digit numbers. Define a function f(expression) that returns the value of the expression. Sample result:

#f("2+3") returns 5
#f("3+8+1") returns 12
#f("2+3-4+5-0") returns 6

def f(expression): # Funkcja przyjmuje działanie zapisane jako tekst, np. "2+3".
    result = 0 # Na początku wynik wynosi 0.
    sign = 1 # Pierwszą cyfrę domyślnie dodajemy.

    for char in expression:  # Przechodzimy po kolei przez każdy znak tekstu.
        if char == "+":  # Sprawdzamy, czy bieżący znak to plus.
            sign = 1 #Zapamiętujemy, że następną cyfrę dodamy.
        elif char == "-": # Sprawdzamy, czy bieżący znak to minus.
            sign = -1 # Zapamiętujemy, że następną cyfrę odejmiemy.
        else: # W tym miejscu zakładamy, że bieżący znak to cyfra.
            result += sign * int(char) # Zamieniamy cyfrę na liczbę i dodajemy ją ze znakiem + lub -.

    return result # Po przejściu przez cały tekst zwracamy końcowy wynik.

#Na przykład gdy pętla napotka -, ustawia sign = -1. Gdy w kolejnym obrocie napotka "4", oblicza -1 * 4, więc result += -4 zmniejsza wynik o 4.


print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))