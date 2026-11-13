#Write a program that converts a decimal number into a binary number. To convert a decimal number to binary, follow these steps:

#Read a decimal number from the keyboard.
#Divide the number by 2 and note the remainder.
#Divide the quotient obtained by 2 and note the remainder.
#Repeat the same process till we get 0 as the quotient.
#Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
#Sample result:

#Enter decimal number: 12
#12(10) = 1100(2)

x = int(input("Enter decimal number: "))
binary = '' #puste
while x >0 : # sprawdza czy wieksze od 0
   y = x % 2 # oblicza resztę z dzielenia przez 2 i zapisuje ją w y
   x = x // 2 # dzieli x przez 2 całkowitoliczbowo i zapisuje wynik w x
   binary = str(y) + binary  # zamienia resztę na tekst i dopisuje ją z przodu wyniku

print(binary)
