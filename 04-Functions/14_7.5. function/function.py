#In a separate module, define a function that checks if the number is within the range <x, y>. The function returns a boolean value. Then, create a program and use the function you defined. Sample result:

import module_function # Importujemy moduł, w którym znajduje się funkcja in_range.

number = 7 # sprawdzamy tą liczbę
x = 2 #dolna granica
y= 15 #górna granica

result = module_function.in_range(number,x,y) # Zapisujemy wynik sprawdzenia (True albo False).

if result == True:
    result = "yes" #wyświetlamy true jak yes
else:
    result = "no"

print(f'Number: {number}')
print(f'Number {number} in the range <{x},{y}>: {result}.')