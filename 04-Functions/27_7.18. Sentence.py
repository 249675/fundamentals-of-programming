#A sentence is an ordered group of words separated by spaces. Define a function f(sentence) that returns a sentence with spaces removed. Sample result:

#f("integrated development environment") returns
#"integrateddevelopmentenvironment"
#f("A programming language is a system of notation for writing
#computer programs") returns
#"Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"

def f(sentence):
    result = ""  # Zaczynamy od pustego tekstu.
    for char in sentence: # Przechodzimy po kolei przez każdy znak zdania.
        if not char == " ": # Sprawdzamy, czy bieżący znak jest inny niż spacja.
            result += char # Dopisujemy ten znak na końcu wyniku.
    return result # Zwracamy gotowy tekst bez spacji.

print (f("integrated development environment"))
print (f("A programming language is a system of notation for writing computer programs"))

