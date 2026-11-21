#The files.txt contains a list of file names. 
# Write a program that prints only those file names whose extensions consist of exactly four characters (e.g. .html).


import re  # Importujemy moduł do obsługi wyrażeń regularnych.

with open("files.txt") as file:  # Otwieramy plik z listą nazw.

    for line in file:  # Odczytujemy po kolei każdy wiersz.

        file_name = line.rstrip("\n")  # Usuwamy znak końca wiersza.

        if re.search(r"\.[^.\s]{4}$", file_name):  # Sprawdzamy, czy rozszerzenie ma dokładnie 4 znaki.
            print(file_name)  # Wypisujemy całą nazwę pasującego pliku.

#\. dopasowuje kropkę.
#[^.\s] dopasowuje znak inny niż kropka i biały znak, np. spacja.
#{4} wymaga dokładnie czterech takich znaków.
#$ oznacza koniec nazwy, więc po tych czterech znakach nic już nie może wystąpić.       





