# Write a program that asks the user for their age and then checks which age group they belong to:

# Child: under 13
# Teen: 13 to 19
# Adult: 20 to 64
#Senior: 65 or older


Age = int(input("Please enter your age: "))

if Age < 13 :
    print("Child")
elif Age >=13 and Age <= 19:
    print("Teen")
elif Age >=20 and Age <=64:
    print ("Adult")
elif Age >= 65:
    print("Senior")