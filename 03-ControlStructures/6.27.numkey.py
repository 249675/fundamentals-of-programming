#A computer numeric keyboard has the arrangement of the keys as below. The included program code prints the computer keyboard. Analyse the program in terms of the printed results. Do you understand each program statement? Then make changes in your program code. Replace the 'for' with a 'while' statement.

#7 8 9
#4 5 6
#1 2 3

for i in range(6,-1,-3): # zaczynamy od 6, liczby idą w dół bo -1, skok o 3 pola w dół bo -3)
    for j in range(1,4): #następnie bierzemy petle for wewnatrz tej petli z numeracja 1 2 3
        print(f'{i+j}',end=' ') # dodajemy do 0 - 1 2 3 , do 3, 1 2 3 , do 6 1 2 3 i mamy 3x3. end robi spacje pomiedzy
    print()

print("=============================================")


i = 6
while i >=0:
    j = 1
    while j <= 3:
        print(f'{i+j}', end=' ')
        j += 1 
    print()
    i -= 3