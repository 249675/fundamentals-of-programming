#A computer numeric keyboard has the arrangement of the keys as below. The included program code prints the computer keyboard. Analyse the program in terms of the printed results. Do you understand each program statement? Then make changes in your program code. Replace the 'for' with a 'while' statement.

#7 8 9
#4 5 6
#1 2 3

for i in range(6,-1,-3): # i przyjmuje kolejno 6, 3, 0; zmniejszamy o 3, granica -1 jest wykluczona
    for j in range(1,4): # dla każdego i zmienna j przyjmuje kolejno 1, 2, 3
        print(f'{i+j}',end=' ') # wypisuje sumę i+j oraz spację zamiast przejścia do nowej linii
    print() #po zakończeniu wewnętrznej pętli przechodzi do nowego wiersza

print("=============================================")


i = 6
while i >=0: # powtarza pętlę, dopóki i jest większe lub równe 0
    j = 1 # na początku każdego wiersza ustawia j z powrotem na 1
    while j <= 3: # dla każdego i zmienna j przyjmuje kolejno 1, 2, 3
        print(f'{i+j}', end=' ') # wypisuje sumę i+j oraz spację zamiast nowej linii
        j += 1  # zwiększa j o 1, żeby przejść do następnej liczby w wierszu
    print() # po zakończeniu wewnętrznej pętli przechodzi do nowego wiersza
    i -= 3 # zmniejsza i o 3: z 6 na 3, potem na 0, a następnie na -3