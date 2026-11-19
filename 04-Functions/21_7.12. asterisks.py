#Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:

#f(4) returns "*/*/*/*"
#f(1) returns "*"


def f(n):
    result = "" # Zaczynamy od pustego tekstu.
    for i in range (n): # Wykonujemy pętlę n razy. Indeks i zaczyna się od 0.
        if i > 0: # Sprawdzamy, czy dodaliśmy już pierwszą gwiazdkę.
            result += "/" # Dodajemy ukośnik przed każdą kolejną gwiazdką.
        result += "*" # Dodajemy jedną gwiazdkę w każdym obrocie pętli.


    return result # Zwracamy gotowy tekst.

print (f(4))
print (f(1))
        
    
