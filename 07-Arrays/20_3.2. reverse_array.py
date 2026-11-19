# An array contains natural numbers: 15, 8, 31, 47, 2, 19.
# Create a program that prints the contents of the array in reverse order.
# Use any loop statement.

numbers = [15, 8, 31, 47, 2, 19]
reversed_numbers = [] # Tworzymy pustą listę na liczby w odwrotnej kolejności.

for index in range(len(numbers) - 1, -1, -1): # Przechodzimy od ostatniego indeksu do 0.(pierwsze -1 - tu zaczynamy, ostatni znak array, drugie -1 granica, czyli konczymy na -1. 0(czyli 1szy elemtn) uwzględniamy., trzecie -1 to skok o 1 w dół)
    reversed_numbers = reversed_numbers + [numbers[index]] # Łączymy zebraną listę z listą zawierającą jedną liczbę i zapisujemy wynik.

print("existed array:", end=" ")  # Wyświetlamy etykietę i zostajemy w tym samym wierszu.
for number in numbers:
    print(number, end=" ")  # Wyświetlamy każdą liczbę i dodajemy po niej spację.
print()

print("reverse array:", end=" ")  # Wyświetlamy etykietę drugiego wiersza.
for number in reversed_numbers:
    print(number, end=" ")  # Wyświetlamy kolejne liczby z odwróconej listy.
print()  # Kończymy drugi wiersz.