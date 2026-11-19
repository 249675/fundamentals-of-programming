#Define the function f(n), which returns the n-th value of the Fibonacci sequence. The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. Each subsequent value is the sum of the previous two. Sample result:

#f(5) returns 3
#f(9) returns 21

def f(n):
    a = 0 # Pierwszy wyraz ciągu.
    b = 1 # Drugi wyraz ciągu.

    if n == 1: # Jeśli szukamy pierwszego wyrazu, od razu zwracamy 0.
        return a
    
    for i in range(n-2): # Mamy już dwa wyrazy, więc wykonujemy n - 2 kroków.
        c = a + b # Obliczamy kolejny wyraz jako sumę dwóch poprzednich.
        a = b # Przesuwamy się o jeden wyraz dalej.
        b = c  # Zapisujemy nowo obliczony wyraz jako bieżący.
        
    return b  # Zwracamy wyraz na pozycji n.


print (f(1))
print (f(2))
print (f(5))
print (f(9))