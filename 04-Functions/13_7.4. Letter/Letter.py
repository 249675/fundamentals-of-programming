#Write a program that calculates how many times the given letter appears in any text. Then create a program and check how many times the letter 'e' appears in the text below. In a separate module, define a function for making calculations. Sample result:

import Module_Letter as count # Importujemy moduł pod krótszą nazwą „count”.

text = "You never get a second chance to make a first impression"  # Zapisujemy zdanie do sprawdzenia.

result = count.count_letter(text, "e")  # Wywołujemy funkcję z modułu i zapisujemy liczbę wystąpień litery „e”.

print(text) # Wyświetlamy zdanie.
print(f'Letter e appears {result} times in text above.')  # Wstawiamy wynik do komunikatu i go wyświetlamy.