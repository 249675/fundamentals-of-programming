# Write a program to separate even and odd numbers in an array of integers.
# Put all even numbers first, and then all odd numbers.
# Sample array: [7, 9, 2, 4, 5, 6]
# Sample result: [2, 4, 6, 7, 9, 5]

numbers = [7, 9, 2, 4, 5, 6]
even_numbers = [] # Pusta lista na liczby parzyste.
odd_numbers = [] # Pusta lista na liczby nieparzyste.

print("arr =", numbers) # Wyświetlamy listę w pierwotnej kolejności.

for number in numbers: # Pobieramy po kolei każdą liczbę z listy.
    if number % 2 == 0:
        even_numbers = even_numbers + [number]  # Dołączamy ją do listy liczb parzystych.
    else:
        odd_numbers = odd_numbers + [number]  # Dołączamy ją do listy liczb nieparzystych.

numbers = even_numbers + odd_numbers  # Łączymy listy, zaczynając od liczb parzystych.
print("arr =", numbers)  # Wyświetlamy wynik.