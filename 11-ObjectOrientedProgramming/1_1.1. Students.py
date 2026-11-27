#The file student.py contains the definition of a class that contains attributes describing a student. 
# Modify the class by adding a third attribute. Then make changes to the program by adding a third student. 
# Assign values ​​of all available attributes to all students. Finally, print information about all students.

# Klasa opisuje dane jednego studenta.
class Student():  # Tworzymy klasę Student — wzór, na podstawie którego będziemy tworzyć obiekty.
    def __init__(self):  # Metoda uruchamiana automatycznie przy tworzeniu każdego obiektu Student. # __ przed i po __ musi być. Tak działają klasy init
        self.name = "" #puste
        self.age = 0 #puste
        self.course = ""  # Każdy obiekt ma własny kierunek studiów.

def main():
    # Tworzymy trzy osobne obiekty i przypisujemy im dane.
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student2.name = "Olivia"
    student2.age = 21
    student1.course = "Computer Science"
    student2.course = "Economics"

    student3.name = "Wojciech"
    student3.age = 23
    student3.course = "Mathematics"

    print('LIST OF STUDENTS')
    print('================')

    # Pętla wypisuje te same trzy atrybuty dla każdego studenta.
    for student in [student1, student2, student3]:
        print(f"{student.name}, {student.age} years old, {student.course}")


if __name__ == "__main__":
    main()
