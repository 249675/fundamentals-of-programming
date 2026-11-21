#Using a queue, write a program that manages a queue of files to print.

import queue  # Importujemy moduł do obsługi kolejek.

files_to_print = queue.Queue()  # Tworzymy pustą kolejkę na nazwy plików.

while True:  # Wyświetlamy menu w kółko, dopóki użytkownik nie wybierze 0.
    print("1. Add file to print")  # Opcja dodania pliku do kolejki.
    print("2. Print file")  # Opcja obsłużenia następnego pliku.
    print("0. Quit")  # Opcja zakończenia programu.
    menu = input("Select an option: ")  # Pobieramy wybór użytkownika jako tekst.

    if menu == "1":
        file_name = input("Enter file name to print: ").strip()  # Pobieramy nazwę i usuwamy spacje z jej początku i końca.
        if file_name:  # Sprawdzamy, czy po usunięciu spacji nazwa nadal zawiera jakieś znaki.
            files_to_print.put(file_name)  # Dodajemy nazwę pliku na koniec kolejki.

    elif menu == "2":
        if files_to_print.empty():  # Sprawdzamy, czy kolejka jest pusta.
            print("The print queue is empty.")  # Informujemy, że kolejka nie zawiera plików.
        else:
            file_name = files_to_print.get()  # Pobieramy i usuwamy pierwszą nazwę z kolejki.
            print(f"File {file_name} is currently being printed. Please wait!")  # Symulujemy drukowanie komunikatem.

    elif menu == "0":
        break  # Wychodzimy z pętli i kończymy program.