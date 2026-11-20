# A matrix is a rectangular array of values arranged in rows and columns.
# Create a function identity_matrix(n) that returns an identity matrix
# of size n. Create a second function that prints a 2D array in rows
# and columns. Print identity matrices of sizes 3, 5 and 8.

def identity_matrix(n):  # Tworzymy macierz jednostkową o wymiarach n × n.
    matrix = []  # Zaczynamy od pustej listy wierszy.

    for row_index in range(n):  # Tworzymy po jednym wierszu dla każdego indeksu.
        row = [0] * n  # Tworzymy nowy wiersz z n zerami.
        row[row_index] = 1  # Wstawiamy 1 w kolumnie o tym samym indeksie co wiersz.
        matrix = matrix + [row]  # Dołączamy cały wiersz jako jeden element macierzy.

    return matrix  # Zwracamy gotową macierz.


def print_matrix(matrix):  # Wypisujemy macierz w wierszach i kolumnach.
    for row in matrix:  # Pobieramy kolejny wiersz.
        for value in row:  # Pobieramy kolejne liczby z tego wiersza.
            print(value, end=" ")  # Wypisujemy liczbę i spację w tym samym wierszu.
        print()  # Po całym wierszu przechodzimy do następnej linii.


for size in (3, 5, 8):  # Tworzymy i wyświetlamy kolejno trzy macierze.
    print_matrix(identity_matrix(size))
    print()  # Oddzielamy macierze pustą linią.

    #Dla n = 3 linia row[row_index] = 1 ustawia jedynkę kolejno pod indeksem 0, 1 i 2 w kolejnych wierszach. Tak powstaje główna przekątna.