#Write a program that calculates the number of lines, characters and words for any text file. 
# The user enters the name of the file from the keyboard. Use a try-except block to avoid interrupting your 
# program when the user enters a filename that doesn't exist. Print the result of the calculation. 
# To check if the program is working correctly, find 3 text files on the Internet and use them to test the program.Sample result:

#File name: books.txt
#Number of lines: 14
#Number of characters: 2540
#Number of words: 703


file_name = input("File name: ") # Pobieramy nazwę pliku, np. pets.txt.

try:  # Próbujemy otworzyć i odczytać plik.
    with open(file_name) as file: # Otwieramy plik tekstowy do odczytu
        content = file.read() # Wczytujemy cały tekst. Po wyjściu z with plik zamknie się automatycznie.

    print("Number of lines:", len(content.splitlines())) # Dzielimy tekst na wiersze i je liczymy.
    print("Number of characters:", len(content))  # Liczymy także spacje i znaki nowego wiersza.
    print("Number of words:", len(content.split())) # Dzielimy tekst na słowa i je liczymy.
except FileNotFoundError: # Ten blok wykona się, jeśli Python nie znajdzie pliku.
    print("File not found.")
except UnicodeError: # Ten blok wykona się, jeśli zawartości nie da się odczytać jako UTF-8.
    print("The file could not be read as UTF-8 text.")
except OSError: # Ten blok obsługuje inne problemy z plikiem, np. brak uprawnień.
    print("The file could not be opened.")
