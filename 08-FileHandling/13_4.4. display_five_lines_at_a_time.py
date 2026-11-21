#Write a program that displays the first five lines from the it_company.csv file and then prints 'Press Enter key...' in the next line and waits for the Enter key to be pressed. The program repeats printing the next five lines from the file, waiting for the Enter key to be pressed each time.

with open("it_company.csv") as file:
    count = 0

    for line in file: # Pobieramy po kolei każdy wiersz pliku, zaczynając od nagłówka.
        print(line, end="")  # Wypisujemy wiersz bez dodawania kolejnego znaku nowej linii.
        count += 1 # Doliczamy właśnie wyświetlony wiersz.

        if count == 5: # Po wyświetleniu pięciu wierszy robimy pauzę.
            input("Press Enter key...") # Czekamy, aż użytkownik naciśnie Enter.
            count = 0 # Zerujemy licznik przed wypisaniem kolejnej grupy.
