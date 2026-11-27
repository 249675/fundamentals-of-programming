#Write a program containing a Statistics class that describes the properties of any set of numbers. The class should allow to:

#Add to the set of numbers, the next number read from the keyboard (store the numbers in the array)
#Display all numbers separated by a space
#Determine the greatest number
#Determine the smallest number
#Calculate the arithmetic mean of numbers
#Calculate of the median
#Print of calculated / determined statistical quantities (minimum, maximum, arithmetic mean, median)
#Then, use the program for numbers below to calculate and print the basic staticstics:

#12, 37, 6, 9, 17 

class Statistics:
    def __init__(self):
        self.numbers = []  # Lista zachowuje kolejność wpisywania i powtórzenia.

    def add_number(self):
        number = float(input("Enter a number: "))
        self.numbers.append(number)

    def show_numbers(self):
        # end=" " pozwala wypisać następną liczbę w tym samym wierszu.
        for number in self.numbers:
            print(number, end=" ")
        print()

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)

    def mean(self):
        # Średnia to suma podzielona przez liczbę elementów.
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        ordered = sorted(self.numbers)  # Sortujemy kopię, zachowując kolejność wejścia.
        count = len(ordered)
        middle = count // 2  # Dzielenie całkowite daje indeks środkowej pozycji.
        if count % 2 == 1:
            return ordered[middle]
        # Dla parzystej liczby elementów bierzemy średnią dwóch środkowych.
        return (ordered[middle - 1] + ordered[middle]) / 2

    def show_statistics(self):
        if not self.numbers:
            print("No numbers entered.")
            return

        print(f"Minimum: {self.minimum():g}")
        print(f"Maximum: {self.maximum():g}")
        print(f"Mean: {self.mean():g}")
        print(f"Median: {self.median():g}")


stats = Statistics()
# Wpisz kolejno 12, 37, 6, 9 i 17, zatwierdzając każdą liczbę Enterem.
for _ in range(5):
    stats.add_number()
stats.show_numbers()
stats.show_statistics()
