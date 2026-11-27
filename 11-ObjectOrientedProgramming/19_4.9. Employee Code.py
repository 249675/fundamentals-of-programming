#An object representing an employee contains the following data: name, surname, age, and seniority (the number of years worked).
#  Define a C class that allows you to create an object. Provide employee data at the time of creating the object, in the given order.
#  Define a text representation of an object in the class that contains a string of last name, first letter of first name, and seniority.
#  If the employee is an adult (at least 18 years old), use uppercase letters, otherwise lowercase letters. Sample result:

#C("Anna","May",17,7) returns "maya7"
#C("George","Brown",21,4) returns "BROWNG4

class C:  # Tworzymy klasę o nazwie C.

    def __init__(self, name, surname, age, seniority):  # Konstruktor przyjmujący cztery argumenty opisujące osobę.
        self.name = name  # Zapisujemy imię osoby.
        self.surname = surname  # Zapisujemy nazwisko osoby.
        self.age = age  # Zapisujemy wiek osoby.
        self.seniority = seniority  # Zapisujemy staż pracy osoby.

    def __str__(self):  # Metoda określająca, jaki tekst zostanie wyświetlony podczas printowania obiektu.
        code = f"{self.surname}{self.name[0]}{self.seniority}"  # Łączymy nazwisko, pierwszą literę imienia oraz staż pracy w jeden napis.

        if self.age >= 18:  # Sprawdzamy, czy osoba ma co najmniej 18 lat.
            return code.upper()  # Zwracamy kod zapisany wielkimi literami.
        return code.lower()  # Jeżeli osoba ma mniej niż 18 lat, zwracamy kod zapisany małymi literami.


print(C("Anna", "May", 17, 7))  # Tworzymy obiekt osoby niepełnoletniej i wyświetlamy jej kod.
print(C("George", "Brown", 21, 4))  # Tworzymy obiekt osoby pełnoletniej i wyświetlamy jej kod.