#Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user. Sample result:

x = int(input("Enter number: "))
for i in range (1,11):
    print(f'{x} x {i} = {x*i}')