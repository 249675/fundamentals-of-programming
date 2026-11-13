#Write a program that checks what number was entered from the keyboard and prints one of the messages below.

number = int(input('Please enter number: '))

if number > 0:
    print (f'Number {number} is positive')
elif number < 0:
    print (f'Number {number} is negative')
elif number == 0:
    print (f'Number is 0')