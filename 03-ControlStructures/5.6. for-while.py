###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10 # tyle liczb sprawdzamy
sum_even = 0 

# Calculate the sum of even numbers
i = 1 #zaczynam od 1 a poźniej sprawdza aż do N
while i <= N: #dopóki mniejsze lub rowne niz n to leci
    if i % 2 == 0: #gdy reszta 0, czyli parzysta
        sum_even += i #dodaje i do zerowego sum_even. czyli łapie parzyste 2 + 4 etc.
    i +=1 #sprawdza kolejne liczby
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")