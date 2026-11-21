#Write a program that converts any natural number to a binary number. Use the stack. To convert a number, divide the number by 2, each time taking the remainder of the division and putting the remainder on the stack. Repeat the division until the number you are dividing is zero. Then pop and display all values from the stack. Sample result for number 18:

#Division	Remainder
#18 / 2 = 9	0
#9 / 2 = 4	1
#4 / 2 = 2	0
#2 / 2 = 1	0
#1 / 2 = 0	1
#Natural number: 18
#Binary number: 10010 

import queue  # Importujemy moduł, z którego użyjemy stosu LIFO.


def to_binary(number):  # Zamieniamy liczbę na zapis binarny i zwracamy go jako tekst.
    if number == 0:  # Dla zera pętla dzielenia nie wykonałaby się ani razu.
        return "0"

    stack = queue.LifoQueue()  # Tworzymy pusty stos na reszty z dzielenia.
    while number > 0:  # Powtarzamy dzielenie, dopóki liczba jest większa od zera.
        stack.put(number % 2)  # Obliczamy resztę z dzielenia przez 2 i odkładamy ją na stos.
        number //= 2  # Zastępujemy liczbę całkowitym wynikiem dzielenia, np. 9 // 2 daje 4.

    result = ""  # Zaczynamy od pustego tekstu.
    while not stack.empty():  # Pobieramy reszty, dopóki na stosie coś zostało.
        result += str(stack.get())  # Zdejmujemy ostatnią dodaną resztę i dopisujemy ją jako tekst.
    return result  # Zwracamy gotowy zapis binarny.


try:
    number = int(input("Natural number: "))  # Pobieramy wpis i zamieniamy go na liczbę całkowitą.
    if number < 0:  # Program oczekuje liczby nieujemnej.
        print("Enter a non-negative integer.")
    else:
        print("Binary number:", to_binary(number))  # Wywołujemy funkcję i wyświetlamy wynik.
except ValueError:  # Obsługujemy wpis, którego int() nie może zamienić na liczbę całkowitą.
    print("Enter a non-negative integer.")