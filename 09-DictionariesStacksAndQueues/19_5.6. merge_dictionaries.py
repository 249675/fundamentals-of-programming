#The program contains two dictionaries with personal data:
#Write a program that creates a dictionary called person containing data from the two other dictionaries (five key-value pairs). Print the contents of the ‘person’ dictionary.



basic_data = {"name": "Barbara", "age": 21}
advanced_data = {"status": "student", "married": False,
                 "interest": ["reading", "swimming"]}

person = {} # Tworzymy pusty słownik, do którego zbierzemy wszystkie dane.
person.update(basic_data)  # Dodajemy pary klucz-wartość z pierwszego słownika. # Dodajemy imię i wiek do słownika person.
person.update(advanced_data) # Dodajemy status, stan cywilny i zainteresowania.
for key, value in person.items():  # W każdym obrocie pobieramy jeden klucz i jego wartość.
    print(f"{key}: {value}") # Wypisujemy każdą parę w osobnym wierszu.
