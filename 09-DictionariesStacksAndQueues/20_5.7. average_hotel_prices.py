#A program contains two functions:

#hotel_list(hotels) that returns a list of hotel names, separated by a comma sign
#avg_price(hotels) that returns the average room price for a given list of hotels, rounded to an integer value
#Write a program that calculates and displays the average price for a room in hotels in Krakow and Sopot and indicates in which cities hotels are cheaper. Sample result:

#Hotels in Krakow: …,…,…,…
#Average hotel price in Krakow: …
#Hotels in Sopot: …,…,…,…
#Average hotel price in Sopot: …
#Cheaper hotels in: …

def hotel_list(hotels):  # Tworzymy tekst z nazwami hoteli oddzielonymi przecinkami.
    result = ""  # Zaczynamy od pustego tekstu.
    for hotel in hotels:  # Pobieramy kolejno słownik każdego hotelu.
        if result != "":  # Sprawdzamy, czy w tekście jest już jakaś nazwa.
            result += ","  # Jeśli tak, dopisujemy przecinek przed kolejną nazwą.
        result += hotel["name"]  # Pobieramy nazwę ze słownika i dopisujemy ją do tekstu.
    return result  # Zwracamy gotowy tekst z nazwami.


def avg_price(hotels):  # Obliczamy zaokrągloną średnią cenę hoteli.
    total = 0  # Zaczynamy sumowanie od zera.
    for hotel in hotels:  # Przechodzimy po wszystkich hotelach.
        total += hotel["price"]  # Pobieramy cenę hotelu i dodajemy ją do sumy.
    return round(total / len(hotels))  # Dzielimy sumę przez liczbę hoteli i zaokrąglamy do liczby całkowitej.


# Każdy hotel opisujemy słownikiem z nazwą i ceną.
hotels_in_krakow = [
    {"name": "Sky", "price": 320}, {"name": "Metropol", "price": 480},
    {"name": "New Port", "price": 420}, {"name": "Aparthotel", "price": 390},
]
hotels_in_sopot = [
    {"name": "Focus", "price": 510}, {"name": "Aqua", "price": 345},
    {"name": "La Boutique", "price": 390}, {"name": "Marina", "price": 410},
]

krakow_price = avg_price(hotels_in_krakow)  # Obliczamy i zapisujemy średnią dla Krakowa.
sopot_price = avg_price(hotels_in_sopot)  # Obliczamy i zapisujemy średnią dla Sopotu.

print("Hotels in Krakow:", hotel_list(hotels_in_krakow))  # Wypisujemy nazwy hoteli w Krakowie.
print("Average hotel price in Krakow:", krakow_price)  # Wypisujemy średnią dla Krakowa.
print("Hotels in Sopot:", hotel_list(hotels_in_sopot))  # Wypisujemy nazwy hoteli w Sopocie.
print("Average hotel price in Sopot:", sopot_price)  # Wypisujemy średnią dla Sopotu.

if krakow_price < sopot_price:  # Sprawdzamy, czy zaokrąglona średnia jest niższa w Krakowie.
    print("Cheaper hotels in: Krakow")
elif sopot_price < krakow_price:  # Sprawdzamy, czy niższa jest średnia w Sopocie.
    print("Cheaper hotels in: Sopot")
else:  # Obie zaokrąglone średnie są równe.
    print("Both cities have the same average price.")