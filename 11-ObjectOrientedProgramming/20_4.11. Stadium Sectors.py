#A stadium is divided into sectors, each marked with a letter. 
# There is a certain number of fans in each sector. Define the class C, 
# which allows you to create an object representing the stadium with a list of sectors and the number of fans in sectors.
# Data, as a dictionary, should be transferred to the object at the time of its creation.
#  Define in the class a method m1(s,n) that allows you to change the number of fans n in sector s or add a new sector s with the given number of fans n. 
# Define in the class a method m2(s) that returns the sum of fans in the sectors listed in the string s. 
# Sample result:

#C({"A":120,"D":150,"G":90,"K":110})
#m1("G",130)
#m2("GD") returns 280
#m2("KEJ") returns 110

class C:  # Tworzymy klasę opisującą stadion.

    def __init__(self, sectors):  # Konstruktor przyjmujący słownik sektorów i liczby kibiców.
        self.sectors = sectors  # Zapisujemy otrzymany słownik w obiekcie.

    def m1(self, s, n):  # Metoda zmieniająca liczbę kibiców lub dodająca nowy sektor.
        self.sectors[s] = n  # Przypisujemy do sektora s liczbę kibiców n.

    def m2(self, s):  # Metoda obliczająca sumę kibiców w podanych sektorach.
        total = 0  # Tworzymy zmienną przechowującą sumę kibiców, początkowo równą 0.

        for sector in s:  # Pobieramy kolejno każdą literę z przekazanego napisu.
            if sector in self.sectors:  # Sprawdzamy, czy dany sektor istnieje w słowniku.
                total += self.sectors[sector]  # Dodajemy liczbę kibiców z danego sektora do sumy.

        return total  # Zwracamy całkowitą liczbę kibiców z wybranych sektorów.


stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})  # Tworzymy obiekt stadionu i przekazujemy słownik sektorów.
stadium.m1("G", 130)  # Zmieniamy liczbę kibiców w sektorze G z 90 na 130.
print(stadium.m2("GD"))  # Obliczamy i wyświetlamy sumę kibiców z sektorów G oraz D.
print(stadium.m2("KEJ"))  # Obliczamy i wyświetlamy sumę kibiców z istniejących sektorów K, E oraz J.