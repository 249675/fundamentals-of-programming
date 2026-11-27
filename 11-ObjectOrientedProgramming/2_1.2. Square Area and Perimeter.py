#The Square class represents objects describing a geometric figure (square). 
# Complete the class by adding a method to calculate the perimeter of a square. 
# Then write a program that creates two squares with sides of 4 and 6, respectively. 
# Calculate the areas and perimeters of these squares. Print the results.

class Square:
    def __init__(self, a):
        self.a = a  # Długość boku konkretnego kwadratu.

    def area(self):
        return self.a * self.a  # Pole to bok pomnożony przez siebie.

    def perimeter(self):
        return 4 * self.a  # Obwód to suma długości czterech równych boków.


square1 = Square(4)
square2 = Square(6)

# Wywołujemy te same metody dla obu kwadratów.
for square in [square1, square2]:
    print(f"Square with side {square.a}:")
    print(f"Area is {square.area()}, Perimeter is {square.perimeter()}.")
