#Define a function that takes a string as input and uses a stack to reverse it. Then, write a program to reverse any text entered from the keyboard.

#Hint: Push each character of the string onto the stack, then pop characters to form the reversed string.

import queue  # Importujemy moduł, z którego użyjemy stosu LIFO.


def reverse_text(text):  
    stack = queue.LifoQueue()  # Tworzymy pusty stos na znaki.
    for char in text:  # Czytamy tekst znak po znaku od początku.
        stack.put(char)  # Kładziemy każdy znak na szczycie stosu.

    reversed_text = ""  # Zaczynamy od pustego tekstu.
    while not stack.empty():  # Powtarzamy, dopóki na stosie są znaki.
        reversed_text += stack.get()  # Zdejmujemy znak ze szczytu i dopisujemy go na końcu wyniku.
    return reversed_text  # Zwracamy gotowy odwrócony tekst.


text = input("Enter text: ")  # Pobieramy tekst z klawiatury.
print("Reversed text:", reverse_text(text))  # Odwracamy tekst i wyświetlamy wynik.
