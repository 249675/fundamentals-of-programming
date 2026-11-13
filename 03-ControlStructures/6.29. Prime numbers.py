#A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. Write a program that finds N leading prime numbers. Read the value of N from the keyboard. Using loop statements check that the number N is divisible only by 1 and by N.

#Prime numbers: 2 3 5 7 11 ...

N = int(input("Enter N number: "))
number = 2
count = 0
while count < N :
    divisors = 0
    for i in range(1,number+1):
        if number % i == 0:
            divisors += 1
    if divisors == 2:
        print (number, end=' ')
        count += 1
    number += 1