#The following array represents a square matrix and contains values:

matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
#Create a program that replaces the values of the main diagonal with 1. Use a loop statement. Print the modified array. Sample result:

#1 0 0
#0 1 0
#0 0 1


for i in range (3): # Zmienna i przyjmuje kolejno wartości 0, 1 i 2.
    matrix[i][i] = 1  # Ustawiamy 1 tam, gdzie indeks wiersza i kolumny jest taki sam.

for row in matrix:  # Pobieramy kolejno każdy wiersz macierzy.
    for value in row:  # Pobieramy każdą wartość z bieżącego wiersza.
        print(value, end=" ")  # Wyświetlamy wartość i spację w tym samym wierszu.
    print()  # Po wypisaniu całego wiersza przechodzimy do następnej linii.