#Create a function f(number, even) that computes the sum of the digits of a number. When the value of the even parameter is True, the function returns the sum of the even digits. When the value of the even parameter is False, the function returns the sum of the odd digits. Sample result:

#f(3124,True) returns 6
#f(3124,False) returns 4
#f(20576,False) returns 12
#f(20576,True) returns 8
#f(13115,True) returns 0


def f(number,even): # Sumujemy cyfry parzyste, gdy even to True, albo nieparzyste, gdy even to False.
    total = 0
    for char in str(number): #Zamieniamy liczbę na tekst i przechodzimy po kolei przez jej cyfry.
        digit = int(char) # Zamieniamy bieżący znak na liczbę całkowitą.
        if digit % 2 == 0 and even == True:  # Sprawdzamy, czy cyfra jest parzysta i czy sumujemy cyfry parzyste.
            total += digit # Dodajemy cyfrę parzystą do sumy.
        elif digit % 2 == 1 and even == False: # Sprawdzamy, czy cyfra jest nieparzysta i czy sumujemy cyfry nieparzyste.
            total +=  digit # Dodajemy cyfrę nieparzystą do sumy.
    return total # Zwracamy sumę wybranych cyfr.

print (f(3124,True))
print(f(3124,False) )
print(f(20576,False) )
print(f(20576,True) )
print(f(13115,True) )