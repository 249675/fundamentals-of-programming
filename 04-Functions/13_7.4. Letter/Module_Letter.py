#Write a program that calculates how many times the given letter appears in any text. Then create a program and check how many times the letter 'e' appears in the text below. In a separate module, define a function for making calculations. Sample result:  

def count_letter(text,letter):  # Funkcja przyjmuje tekst i literę
    count = 0   # Ustawiamy licznik wystąpień na zero.
    for char in text: # Przechodzimy po kolei przez każdy znak tekstu.
        if char == letter: # Sprawdzamy, czy bieżący znak jest szukaną literą.
            count += 1 # Jeśli tak, zwiększamy licznik o 1.
    return count # Po sprawdzeniu całego tekstu zwracamy liczbę wystąpień.
