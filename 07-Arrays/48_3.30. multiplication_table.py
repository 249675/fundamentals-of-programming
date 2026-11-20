# An array of size 5 by 5 is filled with zeros.
# Modify its values to create a multiplication table from 1 to 5.
# Use loop statements and print the array.

table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

for row_index in range(len(table)): # Przechodzimy po indeksach wierszy od 0 do 4.
    for column_index in range(len(table[row_index])):  # Przechodzimy po indeksach kolumn w bieżącym wierszu.
        table[row_index][column_index] = (row_index + 1) * (column_index + 1)  # Dodajemy 1 do obu indeksów, żeby mnożyć liczby od 1 do 5.

for row in table: # Pobieramy po kolei każdy wiersz.
    for value in row: # Pobieramy po kolei każdą liczbę z tego wiersza.
        print(f"{value:2}", end=" ") # Wypisujemy liczbę w polu szerokim na co najmniej 2 znaki, a potem spację. Ta fraza ":2" wyrównuje widok.
    print() # Po wypisaniu całego wiersza przechodzimy do nowej linii.