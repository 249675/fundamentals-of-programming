#As you remember, the input() function allows you to read only a string from the keyboard. In the module keyboard.py, define your own functions that allow reading other types of data from the keyboard:

#input_string() that returns a string entered from the keyboard
#input_integer() that returns an integer number entered from the keyboard
#input_real() that returns a real number entered from the keyboard
#input_boolean() that returns a boolean value depending on the pressed y/n key

###
# Functions to read any data type from the keyboard
#
def input_string(message): # Przyjmujemy komunikat, który wyświetlimy użytkownikowi.
    text = input(message) # Wyświetlamy komunikat i pobieramy wpisany tekst.
    return text

def input_integer(message): # Definiujemy funkcję do wczytywania liczb całkowitych.
    number = int(input(message)) # Pobieramy tekst i zamieniamy go na liczbę całkowitą.
    return number

def input_real(message): # Definiujemy funkcję do wczytywania liczb z częścią ułamkową.
    real = float(input(message)) # Pobieramy tekst i zamieniamy go na liczbę typu float.
    return real

def input_boolean(message): # Definiujemy funkcję, która zwraca True albo False.
    answer = input(message) # Pobieramy odpowiedź użytkownika.
    if answer == "y": # Sprawdzamy, czy użytkownik wpisał dokładnie „y”.
        answer = True
    else:
        answer = False
    return answer
