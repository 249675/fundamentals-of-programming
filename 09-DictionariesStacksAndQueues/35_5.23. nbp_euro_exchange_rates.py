#The website https://api.nbp.pl/en.html contains data on exchange rates published by the National Bank of Poland. The service provides data both in json and xml formats. Display the last ten Euro exchange rates in json format in a web browser. Then, save the data to the euro.json file. Finally, write a program that displays the data from the euro.json file in the following format:

#Date            Buying Rate     Selling Rate
#============================================
#2019-10-25      3.8150          3.9820
#...
#...
#...
#Hint: If you are interested in API and Rest API issues, read the following article: https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/

import json  # Moduł do odczytu i zapisu danych w formacie JSON.
from urllib.error import URLError  # Błąd, który może wystąpić podczas pobierania danych.
from urllib.request import urlopen  # Funkcja do otwierania adresu URL w Pythonie.

# Adres API NBP zwraca 10 ostatnich notowań EUR z tabeli C.
url = "https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json"
file_name = "euro.json"  # Nazwa lokalnego pliku z kursami.


def read_rates():
    try:
        # Najpierw próbujemy odczytać dane z lokalnego pliku.
        # utf-8-sig obsługuje także pliki z dodatkowym znacznikiem BOM na początku.
        with open(file_name, encoding="utf-8-sig") as file:
            return json.load(file)  # Wczytujemy JSON i zwracamy dane jako słownik.
    except FileNotFoundError:
        # Gdy pliku brakuje, pobieramy dane z API NBP z limitem czasu 10 sekund.
        with urlopen(url, timeout=10) as response:
            data = json.load(response)  # Odczytujemy JSON z odpowiedzi NBP.

        # Tworzymy plik i zapisujemy pobrane dane z wcięciami po 4 spacje.
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return data  # Zwracamy pobrane dane, żeby od razu wyświetlić kursy.


try:
    data = read_rates()

    # get() pobiera wartość spod klucza. Jeśli klucza brakuje, zwraca None.
    # Do wyświetlenia kursów potrzebujemy jednocześnie tabeli C i waluty EUR.
    if data.get("table") != "C" or data.get("code") != "EUR":
        print("Use EUR data from NBP table C.")
    else:
        # Dwie pierwsze kolumny wyrównujemy do lewej w polach po 16 znaków.
        print(f"{'Date':<16}{'Buying Rate':<16}{'Selling Rate'}")
        print("=" * 44)  # Powtarzamy znak "=" 44 razy, żeby oddzielić nagłówek.

        for rate in data["rates"]:  # Każdy element listy to jedno notowanie.
            # effectiveDate to data notowania, bid to kurs kupna, ask to kurs sprzedaży.
            # .4f wyświetla kurs z czterema cyframi po kropce.
            print(f"{rate['effectiveDate']:<16}{rate['bid']:<16.4f}{rate['ask']:.4f}")

except (URLError, TimeoutError):
    # Jeśli pobieranie się nie udało, wyświetlamy adres do ręcznego pobrania danych.
    print("Could not reach NBP. Open this URL and save the response as euro.json:")
    print(url)

except (OSError, ValueError, KeyError, TypeError, AttributeError):
    # Obsługujemy m.in. problemy z plikiem, błędny JSON lub brak oczekiwanych pól.
    print("Could not read the EUR rates. Check euro.json.")