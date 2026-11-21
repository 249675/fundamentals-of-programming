#The clothing.csv contains a list of clothing in stock. 
# Write a program that prints those products whose price is less than 60 and whose stock is less than 40.

import csv  # Importujemy moduł do odczytywania plików CSV.
# Otwieramy plik do odczytu. newline="" zostawia obsługę końców wierszy modułowi csv.

with open("clothing.csv", newline="") as file:
    for product in csv.DictReader(file):  # Każdy wiersz danych odczytujemy jako słownik. Klucze to nazwy kolumn.
        price = float(product["Price"])  # Zamieniamy cenę z tekstu na liczbę, np. "29.99" na 29.99.
        stock = int(product["Stock_Quantity"])  # Zamieniamy liczbę sztuk z tekstu na liczbę całkowitą.

        if price < 60 and stock < 40:  # Cena musi być niższa niż 60, a stan magazynowy mniejszy niż 40 sztuk.
            # Wypisujemy nazwę, rozmiar, kolor, cenę i liczbę sztuk.
            # Zapis :.2f wyświetla cenę z dwoma miejscami po kropce.
            print(f"{product['Product_Name']}, {product['Size']}, {product['Color']}, {price:.2f}, {stock}")
