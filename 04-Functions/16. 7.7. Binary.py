#The binary numerical system uses two symbols to represent a number: 0 and 1. Define a function f(binary_number) that returns True if the given string of digits is a valid binary number, or False otherwise. Sample result:

#f("101101") returns True
#f("1311a10100") returns False

def f(binary_number): # Funkcja przyjmuje zapis liczby jako tekst.
    for char in binary_number: # Sprawdzamy po kolei każdy znak.
        if char != "0" and char != "1": # Sprawdzamy, czy znak jest inny niż zarówno „0”, jak i „1”.
            return False # Kończymy sprawdzanie po znalezieniu pierwszego niedozwolonego znaku.
    return True # Jeśli pętla zakończy się bez znalezienia takiego znaku, zwracamy True.

binary_number = "101101"
result = f(binary_number)
print(f'{binary_number}: {result}') # true

binary_number = "1311a10100" 
result = f(binary_number)
print(f'{binary_number}: {result}') # false bo "a"