# Create a function transpose_matrix(m) that returns the transpose of m.
# Print the transposed matrices below in rows and columns.

def transpose_matrix(m):  # Zamieniamy kolumny macierzy na wiersze.
    transposed = []  # Zaczynamy od pustej macierzy wynikowej.

    for column_index in range(len(m[0])):  # Przechodzimy po indeksach kolumn.
        new_row = []  # Każda kolumna utworzy osobny wiersz.
        for row in m:  # Pobieramy po kolei każdy wiersz oryginalnej macierzy.
            new_row = new_row + [row[column_index]]  # Dopisujemy liczbę z wybranej kolumny.
        transposed = transposed + [new_row]  # Dołączamy cały nowy wiersz do macierzy wynikowej.

    return transposed  # Zwracamy macierz po transpozycji.


matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]],
]

for matrix in matrices:  # Bierzemy po kolei każdą macierz.
    for row in transpose_matrix(matrix):  # Przechodzimy po wierszach po transpozycji.
        for value in row:
            print(value, end=" ")  # Wypisujemy liczby w tym samym wierszu.
        print()  # Po całym wierszu przechodzimy do nowej linii.
    print()  # Oddzielamy macierze pustą linią.

#Dla pierwszej macierzy zaczynamy od column_index = 0. Z kolejnych wierszy pobieramy 1, 4 i 7, więc pierwsza #kolumna staje się pierwszym wierszem [1, 4, 7]. Potem tak samo tworzymy [2, 5, 8] i [3, 6, 9].
#[row[column_index]] to lista z jedną liczbą, którą dołączamy do wiersza. [new_row] to lista z jednym całym #wierszem, który dołączamy do macierzy.