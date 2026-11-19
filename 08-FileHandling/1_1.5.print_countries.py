###
# Reads from file, line by line
#

#Modify the program print_countries.py so that the printed list of countries is numbered. Sample result:


with open('countries.txt', 'r') as file:
    number = 1
    for line in file:
        print(f'{number}. {line}', end='')
        number += 1

        #cd 08-FileHandling
        #py 1_1.5.print_countries.py

        #albo

        #Ctrl + Shift + P  - Python: Run Python File in Terminal