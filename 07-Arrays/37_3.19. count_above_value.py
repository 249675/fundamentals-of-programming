# Write a program that, for a given array of real numbers, prints
# the number of elements greater than a value entered from the keyboard.

numbers = [1.5, 8.2, -3.4, 4.0, 6.7]  # Lista liczb do sprawdzenia.
threshold = float(input("Enter a value: "))  # Pobieramy wartość graniczną i zamieniamy ją na liczbę.
count = 0  # Zaczynamy liczenie od zera.

for number in numbers:  # Sprawdzamy po kolei każdą liczbę z listy.
    if number > threshold:  # Sprawdzamy, czy liczba jest większa od wpisanej wartości.
        count += 1  # Jeśli tak, zwiększamy licznik o 1.

print("Array:", numbers)  # Wyświetlamy całą listę z nawiasami i przecinkami.
print("Number of elements greater than the given value:", count)  # Wyświetlamy wynik.