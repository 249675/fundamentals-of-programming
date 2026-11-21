#Write a program that supports customer service in an office. Use the queue. Each new customer receives a ticket with an automatically assigned consecutive number and is added to the end of the queue. The next customer to be served is taken from the beginning of the queue.

import queue  # Importujemy moduł do obsługi kolejek.

customers = queue.Queue()  # Tworzymy pustą kolejkę na numery biletów klientów.
ticket = 1  # Pierwszy klient dostanie bilet z numerem 1.

while True:  # Powtarzamy menu, dopóki użytkownik nie wybierze 0.
    print("1. Add customer")  # Dodaj klienta do kolejki.
    print("2. Serve next customer")  # Obsłuż następnego klienta.
    print("0. Quit")  # Zakończ program.
    choice = input("Select an option: ")  # Pobieramy wybór jako tekst.

    if choice == "1":
        customers.put(ticket)  # Dodajemy numer biletu na koniec kolejki.
        print("Ticket:", ticket)  # Pokazujemy klientowi jego numer.
        ticket += 1  # Przygotowujemy numer biletu dla następnego klienta.

    elif choice == "2":
        if customers.empty():  # Sprawdzamy, czy kolejka jest pusta.
            print("The queue is empty.")
        else:
            # get() pobiera i usuwa pierwszy bilet z kolejki.
            print("Now serving ticket:", customers.get())

    elif choice == "0":
        break  # Wychodzimy z pętli i kończymy program.
