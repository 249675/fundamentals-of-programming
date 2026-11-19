#Define the function f(n) that returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:

#f(1) returns 2
#f(5) returns 11

def f(n):
    count = 0
    number = 2 # zaczynamy od 2 - najmniejsza liczba pierwsza.
    while count < n: # Sprawdzamy kolejne liczby, dopóki nie znajdziemy n liczb pierwszych.
        is_prime = True # Na początku zakładamy, że sprawdzana liczba jest pierwsza.
        for divisor in range(2, number): # Sprawdzamy możliwe dzielniki od 2 do number - 1.
            if number % divisor == 0: # Sprawdzamy, czy liczba dzieli się bez reszty.
                is_prime = False # Znaleziony dzielnik oznacza, że liczba nie jest pierwsza.

        if is_prime == True:  # Jeśli nie znaleźliśmy dzielnika, liczba jest pierwsza.
            count += 1 # Zwiększamy licznik znalezionych liczb pierwszych o 1.
        number += 1 # Przechodzimy do następnej liczby.

    return number -1 # Cofamy ostatnie zwiększenie, żeby zwrócić znalezioną liczbę pierwszą.

print(f(1))
print(f(5))