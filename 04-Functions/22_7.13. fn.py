#Define the function f(n), which returns numbers from 1 to n as a string. Sample result:

#f(11) returns "1234567891011"
#f(4) returns "1234"

def f(n):
    result = ""
    for i in range(1,n+1): # Przechodzimy przez liczby od 1 do n włącznie.
        result += str(i) # Zamieniamy bieżącą liczbę na tekst i dopisujemy ją na końcu.
    return result # Zwracamy gotowy tekst.

print (f(11))
print (f(4))

#i = 1 → result = ""    + "1" → "1"
#i = 2 → result = "1"   + "2" → "12"
#i = 3 → result = "12"  + "3" → "123"
#i = 4 → result = "123" + "4" → "1234"