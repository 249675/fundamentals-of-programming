#Tic-Tac-Toe is a simple yet fun game for two players. You play on a grid of nine squares arranged in three rows and three columns.

#The array below shows a Tic-Tac-Toe board. Write a program that prints a board on the screen.

# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

for row in tic_tac_toe_board: # Zewnętrzna pętla wybiera po kolei każdy wiersz.
   for cell in row: # Wewnętrzna pętla przechodzi po polach bieżącego wiersza.
      print(cell, end=" ") # Wyświetlamy pole i dodajemy po nim spację, zostając w tej samej linii.
   print() # Po wyświetleniu całego wiersza przechodzimy do nowej linii.
   
#Hint: end=" " means that the cursor is not moved to the next line; a space is printed instead