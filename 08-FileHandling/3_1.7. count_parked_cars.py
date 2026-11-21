#The file car_park.txt contains data on the number of parked cars for the last five days. Complete the #following #program to calculate the total number of parked cars.

def read_from_file(name):  # Funkcja przyjmuje nazwę pliku.
    with open(name) as file:  # Otwieramy plik do odczytu.
        content = file.read()  # Wczytujemy całą zawartość jako tekst.
    return content  # Zwracamy odczytany tekst.


file_content = read_from_file("car_park.txt")  # Wczytujemy dane z parkingu.
file_lines = file_content.splitlines()  # Dzielimy tekst na osobne wiersze.

total = 0  # Zaczynamy sumowanie od zera.
for line in file_lines:  # Pobieramy po kolei dane z każdego dnia.
    total += int(line)  # Zamieniamy tekst na liczbę i dodajemy ją do sumy.

print("Total cars parked:", total)  # Po pętli wypisujemy łączną liczbę samochodów.