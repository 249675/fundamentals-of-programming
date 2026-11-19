#A palindrome is an expression that sounds the same when read backwards. Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. Sample result:

#f("radar") returns True
#f("12-11-21") returns True
#f("book") returns False

def f(palindrome):
    backwards = palindrome[::-1] # Tworzymy odwrócony tekst. Krok -1 oznacza odczyt od końca.
    if backwards == palindrome: # Porównujemy odwrócony tekst z oryginałem.
        return True
    else:
        return False

print(f("radar"))
print(f("12-11-21"))
print(f("book"))