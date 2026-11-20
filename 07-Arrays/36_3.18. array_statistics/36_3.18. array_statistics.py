# Create a module MyArrays containing functions for the second largest
# element, the difference between the largest and smallest values, the median,
# the smallest and largest values as a two-element array, and the elements
# as a string separated by minus signs.
# Do not use built-in functions to calculate the results.
# Then write a program that calculates and prints the results for 7,3,8,5,2.

from MyArrays import difference, median, min_max, numbers_as_string, second_largest


numbers = [7, 3, 8, 5, 2]
smallest, largest = min_max(numbers) # Pobieramy minimum i maksimum.

print("Numbers: ", end="")  # Wypisujemy etykietę i zostajemy w tym samym wierszu.
index = 0
for number in numbers:
    if index > 0:
        print(",", end="")  # Wypisujemy przecinek przed każdą liczbą poza pierwszą.
    print(number, end="")  # Wypisujemy liczbę w tym samym wierszu.
    index += 1
print()  # Po wszystkich liczbach przechodzimy do nowego wiersza.

print("Second largest number:", second_largest(numbers))  
print("Difference between largest and smallest:", difference(numbers))  
print("Median:", median(numbers))  
print(f"Smallest and largest number: {smallest},{largest}")  
print("Numbers as a string:", numbers_as_string(numbers)) 