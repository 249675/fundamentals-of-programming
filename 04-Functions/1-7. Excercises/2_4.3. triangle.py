#Define a function triangle_area that calculates and returns the area of ​​a triangle with sides a, b, and c. Use Heron's formula:

#https://en.wikipedia.org/wiki/Heron%27s_formula

#Write a program that calculates the area of ​​a triangle based on the lengths of the triangle's sides read from the keyboard. Use the defined function. Then calculate the area of ​​the triangle for the following dimensions of sides a, b, and c:

#3, 4, 5 (result is 6)
#5, 12, 13 (result is 30)
#7, 24, 25 (result is 84)

def triangle_area(a,b,c): # Definiujemy funkcję, która przyjmuje długości trzech boków trójkąta.
    s = (a+b+c)/2 # Dodajemy długości boków i dzielimy przez 2, żeby obliczyć połowę obwodu.
    P = (s*(s-a)*(s-b)*(s-c))**0.5  # Obliczamy pole ze wzoru Herona. Zapis ** 0.5 oznacza pierwiastek kwadratowy.
    return P

a = 3
b = 4 
c = 5
P = triangle_area(a, b, c)

print(f'The area of ​​a triangle with sides {a}, {b}, {c} is {P}')

a = 5
b = 12 
c = 13
P = triangle_area(a, b, c)

print(f'The area of ​​a triangle with sides {a}, {b}, {c} is {P}')

a = 7
b = 24 
c = 25
P = triangle_area(a, b, c)

print(f'The area of ​​a triangle with sides {a}, {b}, {c} is {P}')