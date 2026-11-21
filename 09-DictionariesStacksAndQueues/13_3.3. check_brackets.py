#Define a function that returns true if the brackets (), {}, [] are used correctly in the given expression. Otherwise, the function returns false. Then write a program that checks the correctness of the expressions given below.

#Use a stack. Read the next characters of the expression. Skip all but the brackets. If it is an opening bracket, put it on the stack. If it is a closing bracket, get the item from the stack and compare whether it is a matching opening bracket.

import queue # Importujemy moduł, z którego użyjemy stosu LIFO.


def brackets_ok(expression): # Sprawdzamy, czy nawiasy w wyrażeniu są poprawnie sparowane.
    stack = queue.LifoQueue() # Tworzymy pusty stos na otwarte nawiasy.
    matching = {")": "(", "]": "[", "}": "{"} # Każdemu zamykającemu przypisujemy pasujący otwierający.

    for char in expression: # Czytamy wyrażenie znak po znaku.
        if char in "([{":  # Jeśli znak jest nawiasem otwierającym, zapamiętujemy go.
            stack.put(char) # Kładziemy nawias na szczycie stosu
        elif char in matching:  # Jeśli znak jest kluczem słownika, jest nawiasem zamykającym.
            # Gdy stos jest pusty, brakuje nawiasu otwierającego.
            # W przeciwnym razie zdejmujemy ostatni otwarty nawias i sprawdzamy, czy pasuje.
            # Ostatni otwarty nawias musi pasować do zamykającego.
            if stack.empty() or stack.get() != matching[char]:
                return False

    return stack.empty()   # True, jeśli na stosie nie zostały żadne niezamknięte nawiasy.


expressions = ["[(2+3)*4+5]/6-{(7*8)+[4]}", "[(2+3]/4)", "(2-3*4+(5/6)"]
for expression in expressions: # Sprawdzamy każde wyrażenie osobno.
    print(f"{expression}: {brackets_ok(expression)}") # Wypisujemy wyrażenie i wynik.

#Najważniejsze jest stack.get() != matching[char]. Weźmy drugie wyrażenie, [(2+3]/4).
#1. [ trafia na stos, a ( ląduje na nim jako ostatni.
#2. Gdy program napotka ], zapis matching[char] daje "[". Takiego nawiasu oczekujemy.
#3. stack.get() zdejmuje jednak "(", bo stos oddaje ostatni dodany element jako pierwszy. Nawiasy się nie zgadzają, więc funkcja zwraca False.
#Jeśli stack.empty() jest True, Python pomija prawą stronę or. Dzięki temu stack.get() nigdy nie próbuje pobrać elementu z pustego stosu.
