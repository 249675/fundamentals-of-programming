#Write a program that calculates a dog's age in dog's years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years. Sample result:

#Enter the dog's age in human years: 15
# The dog's age in dog's years is 73 years.

Age = float(input("Please enter dog's age in human years: "))

if Age > 2:
    Age_above_2 = 10.5 
    print("The dog's age in dogs years is: " f'{Age_above_2 + (Age-2)*4}'"years." )
elif Age == 2: 
    print("The dog's age in dogs years is: 10.5 years")
elif Age < 2:
    Age_above_2 = 10.5 
    print("The dog's age in dogs years is: "f'{Age_above_2 * Age / 2 :.2f}')