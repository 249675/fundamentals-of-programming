#The hotel's IT system contains a list of reserved rooms. The data is contained in the reservations.json file. Write a program that prints the summary information as stated below. Break your program into smaller parts defining functions.

#number of rooms
#number of paid reservations
#number of unpaid reservations
#total value of paid reservations
#total value of unpaid reservations

import json  # Importujemy moduł do odczytu danych w formacie JSON.


def read_reservations(file_name):  # Funkcja przyjmuje nazwę pliku.
    with open(file_name, encoding="utf-8") as file:  # Otwieramy plik do odczytu.
        return json.load(file)["reservations"]  # Wczytujemy słownik i zwracamy listę spod klucza "reservations".


def count_rooms(reservations):  # Liczymy, ile różnych pokoi pojawia się w rezerwacjach.
    room_numbers = set()  # Tworzymy pusty zbiór na numery pokoi.
    for reservation in reservations:  # Pobieramy po kolei słownik każdej rezerwacji.
        room_numbers.add(reservation["room_number"])  # Pobieramy numer pokoju i dodajemy go do zbioru.
    return len(room_numbers)  # Każdy numer pokoju występuje w zbiorze tylko raz.


def payment_summary(reservations, paid):  # Podsumowujemy rezerwacje o wybranym statusie płatności.
    count = 0  # Licznik pasujących rezerwacji.
    total = 0  # Suma wartości pasujących rezerwacji.

    for reservation in reservations:  # Sprawdzamy każdą rezerwację.
        if reservation["paid"] == paid:  # Porównujemy status z pliku z True lub False podanym przy wywołaniu.
            count += 1  # Doliczamy jedną rezerwację.
            # Mnożymy liczbę nocy przez cenę za noc i dodajemy koszt rezerwacji do sumy.
            total += reservation["nights"] * reservation["price_per_night"]

    return count, total  # Zwracamy dwie wartości: liczbę rezerwacji i ich łączną wartość.


reservations = read_reservations("reservations.json")  # Wczytujemy listę rezerwacji z pliku.

paid_count, paid_total = payment_summary(reservations, True)  # Liczymy i sumujemy opłacone rezerwacje.
unpaid_count, unpaid_total = payment_summary(reservations, False)  # Liczymy i sumujemy nieopłacone rezerwacje.

print("Number of rooms:", count_rooms(reservations))  # Wypisujemy liczbę różnych pokoi.
print("Number of paid reservations:", paid_count)  # Wypisujemy liczbę opłaconych rezerwacji.
print("Number of unpaid reservations:", unpaid_count)  # Wypisujemy liczbę nieopłaconych rezerwacji.
print(f"Total value of paid reservations: {paid_total:.2f}")  # Wypisujemy sumę opłaconych z dwoma miejscami po kropce.
print(f"Total value of unpaid reservations: {unpaid_total:.2f}")  # Tak samo wypisujemy sumę nieopłaconych.

# W reservation["paid"] == paid lewa strona to status konkretnej rezerwacji, a prawa to status, którego szukamy. Gdy wywołujesz funkcję z True,
# opłacona rezerwacja na 3 noce po 100 zwiększa count o 1, a total o 300. Na końcu pierwsza zwrócona wartość trafia do paid_count, 
# a druga do paid_total.
