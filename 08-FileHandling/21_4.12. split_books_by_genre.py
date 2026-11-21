#The file books.csv contains a list of books. Write a program that copies the book data from a given genre to its corresponding file. 
# Use functions to divide the program into logical parts.

#Genre --> Filename
#Fantasy --> books_fantasy.txt
#Historical --> books_historical.txt
#Romance --> books_romance.txt
#Classic --> books_classic.txt  

import csv  # Importujemy moduł do odczytu i zapisu danych CSV.


def read_books(file_name):  # Wczytujemy książki z podanego pliku.
    books = []  # Tworzymy pustą listę na dane książek.
    with open(file_name, newline="") as file:  # Otwieramy plik do odczytu.   
        # Zachowujemy En­tery z pliku w oryginalnej postaci.
        # DictReader użyje ich do odczytania kolejnych wierszy CSV.
        for book in csv.DictReader(file):  # Każdy wiersz danych odczytujemy jako słownik.
            books = books + [book]  # Dodajemy cały słownik książki jako jeden element listy.
    return books  # Zwracamy listę wszystkich książek.


def write_genre(books, genre, file_name):  # Zapisujemy książki wybranego gatunku.
    with open(file_name, "w", newline="") as file:  # Tworzymy plik wynikowy lub nadpisujemy jego zawartość.
        # Ustalamy, które pola zapisać i w jakiej kolejności.
        writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Genre", "Year"])

        for book in books:  # Sprawdzamy po kolei każdą książkę.
            if book["Genre"] == genre:  # Porównujemy gatunek książki z gatunkiem podanym w wywołaniu.
                writer.writerow(book)  # Zapisujemy dane pasującej książki w jednym wierszu. #od razu zapisuje ten gatunek książki jako jeden wiersz w pliku.


books = read_books("books.csv")  # Wczytujemy listę książek tylko raz.

write_genre(books, "Fantasy", "books_fantasy.txt")  # Zapisujemy książki fantasy.
write_genre(books, "Historical", "books_historical.txt")  # Zapisujemy książki historyczne.
write_genre(books, "Romance", "books_romance.txt")  # Zapisujemy romanse.
write_genre(books, "Classic", "books_classic.txt")  # Zapisujemy klasykę.
