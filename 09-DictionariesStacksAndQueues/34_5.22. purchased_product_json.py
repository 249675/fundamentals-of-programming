#Write a program that takes data from the keyboard about a purchased product:

#name
#price (real number with two decimal places)
#paid (yes/no)
#The program then saves the product data in the product.json file. Pay attention to the correct data types describing the product (string, #float, bool).

import json  # Moduł do zapisywania danych w formacie JSON.
import math  # Moduł z funkcją, która sprawdza, czy liczba jest skończona.

# input() zwraca tekst, a strip() usuwa spacje z początku i końca wpisu.
name = input("Product name: ").strip()

# Zamieniamy przecinek na kropkę, więc można wpisać np. 12,50 albo 12.50.
price_text = input("Price: ").strip().replace(",", ".")

# lower() zamienia litery na małe, więc np. "YES" staje się "yes".
paid_text = input("Paid (yes/no): ").strip().lower()

try:
    price = float(price_text)  # Zamieniamy tekst na liczbę typu float.

    # Odrzucamy liczby ujemne oraz specjalne wartości, np. inf i nan.
    if not math.isfinite(price) or price < 0:
        print("Enter a valid non-negative price.")
    elif paid_text not in ("yes", "no"):  # Akceptujemy tylko "yes" i "no".
        print("Enter yes or no.")
    elif not name:  # Sprawdzamy, czy nazwa jest pusta.
        print("Enter a product name.")
    else:
        # Tworzymy słownik z trzema polami o różnych typach.
        product = {
            "name": name,                  # str, czyli tekst.
            "price": round(price, 2),      # float zaokrąglony do dwóch miejsc po kropce.
            "paid": paid_text == "yes",    # bool, czyli True dla "yes" i False dla "no".
        }

        # Tryb "w" tworzy plik albo nadpisuje jego zawartość.
        with open("product.json", "w", encoding="utf-8") as file:
            # Zapisujemy słownik do pliku. Zachowujemy polskie litery i robimy wcięia po 4 spacjec.
            json.dump(product, file, ensure_ascii=False, indent=4)

        # :.2f wyświetla cenę w konsoli z dokładnie dwiema cyframi po kropce.
        print(f"Saved to product.json. Price: {product['price']:.2f}")
except ValueError:
    # Tu trafimy np. wtedy, gdy float() spróbuje zamienić tekst "abc" na liczbę.
    print("Enter a valid price.")
