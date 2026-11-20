# An array contains the integers [[-38, 19], [5, 40], [-7, 11], [29, 16]].
# Find the smallest and largest values and print the row and column
# in which each is located.

array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]
smallest = array[0][0] # Na start zapisujemy pierwszą liczbę (-38) jako minimum.
largest = array[0][0] # Tę samą liczbę zapisujemy jako początkowe maksimum.
min_row, min_column = 1, 1 # Początkowe minimum jest w pierwszym wierszu i pierwszej kolumnie.
max_row, max_column = 1, 1  # Początkowe maksimum jest w tym samym miejscu.

for row_number, row in enumerate(array, start=1): # Pobieramy numer wiersza i cały wiersz.
    for column_number, value in enumerate(row, start=1): # Pobieramy numer kolumny i liczbę.
        if value < smallest: # Sprawdzamy, czy znaleźliśmy mniejszą liczbę.
            smallest = value  # Zapisujemy nowe minimum.
            min_row, min_column = row_number, column_number # Zapamiętujemy jego położenie.

        if value > largest:  # Sprawdzamy, czy znaleźliśmy większą liczbę.
            largest = value # Zapisujemy nowe maksimum.
            max_row, max_column = row_number, column_number # Zapamiętujemy jego położenie.

print(f"Smallest value: {smallest}, row {min_row}, column {min_column}") 
print(f"Largest value: {largest}, row {max_row}, column {max_column}")

#enumerate(..., start=1) daje numer i element. Dla drugiego wiersza row_number to 2, a row to [5, 40]. #Wewnętrzna pętla najpierw daje column_number = 1 i value = 5, a potem column_number = 2 i value = 40.
#Dlatego w array[0][0] używasz indeksów od zera, a w wyniku podajesz numery wierszy i kolumn od jedynki.