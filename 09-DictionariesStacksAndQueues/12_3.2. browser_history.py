#A back.py program simulates the Back key in a web browser (recording the name of new website or displaying the previously visited web site). Complete the program.

import queue  # Importujemy moduł, z którego użyjemy stosu LIFO.

visited_websites = queue.LifoQueue()  # Tworzymy pusty stos na historię odwiedzonych stron.
visited_websites.put("instagram.com")  # Dodajemy najstarszą stronę do historii.
visited_websites.put("uek.krakow.pl")  # Dodajemy kolejną stronę na szczyt stosu.
visited_websites.put("microsoft.com")  # Dodajemy najnowszą stronę. To do niej wrócimy najpierw.

current_website = ""  # Na początku nie mamy ustawionej bieżącej strony.

while True:  # Powtarzamy pytanie o adres, dopóki nie wykonamy break.
    website = input("Enter website name (0 for back): ").strip()  # Pobieramy wpis i usuwamy skrajne spacje.

    if website == "0":  # Wpisanie 0 oznacza „Wstecz”.
        if visited_websites.empty():  # Sprawdzamy, czy stos historii jest pusty.
            break  # Jeśli nie ma już dokąd wrócić, kończymy program.

        print("<-- Going back to a previously visited website")  # Informujemy o cofnięciu.
        current_website = visited_websites.get()  # Zdejmujemy ostatnio dodaną stronę ze stosu i ustawiamy ją jako bieżącą.

    elif website != "":  # Użytkownik wpisał adres nowej strony.
        if current_website:  # Sprawdzamy, czy jest już ustawiona bieżąca strona.
            visited_websites.put(current_website)  # Zapisujemy w historii stronę, którą właśnie opuszczamy.
        current_website = website  # Ustawiamy wpisany adres jako bieżącą stronę.

    else:  # Wpis jest pusty.
        continue  # Pomijamy wypisywanie i od razu ponawiamy pytanie o adres.

    print("You are currently viewing:", current_website)  # Wypisujemy adres bieżącej strony.
    print()  # Dodajemy pusty wiersz przed kolejnym pytaniem.
