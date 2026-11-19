#A valid password should consist of at least six characters and each character appears only once in the password. Define a function f(password) that returns True if the password is correct or False otherwise. Sample result:

#f("ax15") returns False
#f("book123") returns False
#f("A2water3") returns True
#f("qwerty") returns True
#f("") returns False

def f(password):
    if len(password) < 6:  # Sprawdzamy długość hasła.
        return False

    for char in password: # Przechodzimy po kolei przez każdy znak hasła.
        if password.count(char) > 1: # Sprawdzamy, czy ten znak występuje więcej niż raz.
            return False

    return True # Hasło ma odpowiednią długość i wszystkie jego znaki są różne.


print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))