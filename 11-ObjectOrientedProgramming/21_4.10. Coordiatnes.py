#An object contains a list of coordinates of points on the plane, as a two-dimensional array. 
# Define a C class that allows you to create an object. Provide the list of coordinates of points at the time of creating the object.
#  In the class C, define a method m(n) that returns true when at least n points are in the first 
# quadrant of the coordinate system (both point coordinates are greater than 0), or false otherwise. Sample result:

#C([[2,3],[1,8],[-6,4],[3,-7]])
#m(2) returns True
#m(3) returns False

class C:  # Tworzymy klasę przechowującą współrzędne punktów.

    def __init__(self, points):  # Konstruktor przyjmujący dwuwymiarową listę punktów.
        self.points = points  # Zapisujemy otrzymaną listę punktów w obiekcie.

    def m(self, n):  # Metoda sprawdzająca, czy co najmniej n punktów znajduje się w pierwszej ćwiartce.
        count = 0  # Tworzymy licznik punktów, początkowo równy 0.

        for point in self.points:  # Pobieramy kolejno każdy punkt z listy.
            x = point[0]  # Pobieramy pierwszy element punktu, czyli współrzędną x.
            y = point[1]  # Pobieramy drugi element punktu, czyli współrzędną y.

            if x > 0 and y > 0:  # Sprawdzamy, czy obie współrzędne są większe od 0.
                count += 1  # Jeżeli oba warunki są spełnione, zwiększamy licznik o 1.

        return count >= n  # Zwracamy True, jeżeli licznik jest większy lub równy n, w przeciwnym razie False.


points = C([[2, 3], [1, 8], [-6, 4], [3, -7]])  # Tworzymy obiekt zawierający listę czterech punktów.

print(f"C({points.points})".replace(" ", ""))  # Wyświetlamy listę punktów i usuwamy wszystkie spacje.
print(f"m(2) returns {points.m(2)}")  # Sprawdzamy, czy co najmniej 2 punkty znajdują się w pierwszej ćwiartce.
print(f"m(3) returns {points.m(3)}")  # Sprawdzamy, czy co najmniej 3 punkty znajdują się w pierwszej ćwiartce.