#The file taxi.py contains the definition of a class describing taxi rides. 
# Complete the class by adding a method print_receipt(self) that prints receipt. 
# It should contain all the information about the ride: distance, rate, and fare. 
# Then write a program in which you create two objects representing two different taxi rides. 
# Calculate the fares for the two rides and print receipts.

class TaxiRide:  # Klasa opisuje jeden przejazd taksówką.
    def __init__(self, rate_per_km):  # Przy tworzeniu przejazdu Python wywołuje tę metodę. self oznacza ten konkretny przejazd.
        self.rate_per_km = rate_per_km  # Stawkę podaną w nawiasie przy TaxiRide(...) zapisujemy w tym obiekcie.
        self.distance = 0  # Początkowy dystans wynosi 0 km.
        self.fare = 0  # Początkowa opłata wynosi 0 euro.

    def calculate_fare(self, distance):  # Metoda oblicza opłatę. distance to liczba kilometrów podana przy wywołaniu.
        self.distance = distance  # Zapisujemy podany dystans w obiekcie, żeby później wyświetlić go na rachunku.
        self.fare = self.distance * self.rate_per_km  # Mnożymy dystans przez stawkę i zapisujemy wynik jako opłatę.

    def print_receipt(self):  # Metoda wyświetla rachunek za przejazd wskazany przez self.
        print(f"Distance: {self.distance} km")  # W miejsce {self.distance} wstawiamy dystans tego przejazdu.
        print(f"Rate: €{self.rate_per_km:.2f}/km")  # Wyświetlamy stawkę za kilometr. Zapis :.2f pokazuje np. 2 jako 2.00.
        print(f"Fare: €{self.fare:.2f}")  # Wyświetlamy obliczoną opłatę z dwoma miejscami po kropce.


def main():  # Definiujemy funkcję, w której tworzymy dwa przejazdy i wyświetlamy ich rachunki.
    ride1 = TaxiRide(2)  # Tworzymy pierwszy przejazd. Liczba 2 trafia do parametru rate_per_km w __init__.
    ride2 = TaxiRide(2.50)  # Tworzymy drugi, osobny przejazd ze stawką 2.50 euro za kilometr.
    ride1.calculate_fare(8)  # Tutaj self to ride1, a distance to 8. Opłata wynosi 8 × 2 = 16 euro.
    ride2.calculate_fare(12)  # Tutaj self to ride2, a distance to 12. Opłata wynosi 12 × 2.50 = 30 euro.
    ride1.print_receipt()  # Wyświetlamy rachunek pierwszego przejazdu (8 km, 16.00 euro).
    print()  # Pusty print() dodaje pustą linię między rachunkami.
    ride2.print_receipt()  # Wyświetlamy rachunek drugiego przejazdu (12 km, 30.00 euro).


if __name__ == "__main__":  # Sprawdzamy, czy ten plik został uruchomiony bezpośrednio.
    main()  # Jeśli tak, uruchamiamy funkcję main().