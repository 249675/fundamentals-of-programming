#Search the Internet and familiarise yourself with RPN (Reverse Polish Notation). Then, write a program that calculates RPN expressions. RPN can be conveniently evaluated using a stack structure. A user can enter from the keyboard any number, an operator (+ - * / ) or the equal sign (=).

#If the entered value is a number, push the number on to the stack
#If the entered value is an operator, pop two items from the top of the stack, do the calculation, and push the result of the operation on to the stack.
#If the entered value is an equal sign, pop the final result from the stack and display the result of calculation.
#Then, using the program, calculate the value of RPN expressions:

#Expression	RPN (Reverse Polish Notation)
#2 + 3 =	2 3 + =
#2 * (4 + 1)	2 4 1 + * =
#(2 + 3) * ( 4 + 5) =	2 3 + 4 5 + * =
#8 / (3 + 1) * (3 - 2 + 4) =	8 3 1 + / 3 2 – 4 + * =

# Operator stoi po argumentach, np. 2 3 + daje 5.
# Źródło: https://en.wikipedia.org/wiki/Reverse_Polish_notation

def calculate(left, right, operator): 
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    return left / right  


stack = []  # Tworzymy pustą listę, której używamy jako stosu.
print("Enter numbers and operators. Use = for the result, or q to quit.")

while True:  # Pobieramy kolejne wpisy, dopóki użytkownik nie wpisze q.
    line = input("RPN: ").strip()  # Usuwamy białe znaki z początku i końca wpisu.
    if line.lower() == "q":  # Zarówno q, jak i Q kończą program.
        break

    for token in line.split():  # Dzielimy wpis na części, np. "8 3 - =" na cztery elementy.
        if token == "=":
            if len(stack) == 1:  # Gotowy wynik to jedna liczba na stosie.
                print(f"Result: {stack.pop()}")  # Pobieramy i usuwamy wynik. :g może wyświetlić 5.0 jako 5.
            else:
                print("The expression must leave exactly one result.")
                stack = []  # Czyścimy stos, żeby zacząć nowe obliczenie.

        elif token in ("+", "-", "*", "/", "–"):  # Sprawdzamy, czy wpisana część to operator.
            if len(stack) < 2:  # Do działania potrzebujemy dwóch liczb.
                print("This operator needs two numbers.")
                continue  # Pomijamy ten operator i przechodzimy do następnej części wpisu.

            # stack[-1] odczytuje ostatnią liczbę bez zdejmowania jej ze stosu.
            if token == "/" and stack[-1] == 0:  # Ostatnia liczba byłaby dzielnikiem.
                print("Cannot divide by zero.")
                continue  # Pomijamy dzielenie i zostawiamy obie liczby na stosie.

            right = stack.pop()  # Zdejmujemy ostatnią liczbę. To prawy argument działania.
            left = stack.pop()  # Zdejmujemy poprzednią liczbę. To lewy argument działania.
            if token == "–":
                token = "-"  # Zamieniamy dłuższą kreskę na zwykły minus.
            stack = stack + [calculate(left, right, token)]  # Dodajemy wynik na szczyt stosu.

        else:  # Próbujemy odczytać wpisaną część jako liczbę.
            try:
                stack = stack + [float(token)]  # Zamieniamy tekst na liczbę i dodajemy ją na koniec listy.
            except ValueError:  # Ten blok wykona się, jeśli float() nie rozpozna liczby.
                print("Unknown token:", token)

# Przykład krok po kroku dla wpisu „8 3 - =”.
# Na początku stos jest pusty: [].
# 1. Program czyta „8” i odkłada liczbę na stos.
#    Stos: [8.0]
# 2. Program czyta „3” i dodaje ją na koniec stosu.
#    Stos: [8.0, 3.0]
# 3. Program czyta „-”, więc potrzebuje dwóch liczb.
#    Pierwsze stack.pop() zdejmuje 3.0. To right, czyli liczba po prawej stronie minusa.
#    Drugie stack.pop() zdejmuje 8.0. To left, czyli liczba po lewej stronie minusa.
#    calculate(8.0, 3.0, "-") oblicza 8.0 - 3.0 i zwraca 5.0.
#    Program odkłada wynik z powrotem na stos: [5.0].
# 4. Program czyta „=” i sprawdza, czy na stosie została dokładnie jedna liczba.
#    Zdejmuje 5.0 ze stosu i wyświetla „Result: 5”.
#    Stos jest znowu pusty: [].