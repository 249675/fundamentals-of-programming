#There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

#Enter the amount in PLN: 18
#The amount of PLN 18 in coins:
#5 PLN coins: 3
#2 PLN coins: 1
#1 PLN coins: 1

Amount = int(input("Enter the amount in PLN: "))
x = Amount // 5 #Szuakmy liczby 5 złotowych monet. Dzielimy kwote przez 5. Ta liczba da nam 5-złotówki
y =  (Amount - x*5)  // 2 #od kwoty odejmujemy liczbę 5-złotówke pomnożoną przez 5. Da nam to pozostałą liczbę z której należy znaleźć 2. Otrzymaną kwotę dzielimy przez 2
z = (Amount - x * 5 - y * 2 ) #Od pełnej kwoty odejmujemy l. 5-złotówek * 5 oraz odejmujemy l. 2-złotówek *2. Pozostała kwota wskaże 1 złotówki

print(f'The amount of PLN {Amount} in coins:')
print(f'5 PLN coins: {x}')
print(f'2 PLN coins: {y}')
print(f'1 PLN coins: {z}')