#A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). Sample result:

#f("Internet of Things") returns "IoT"
#f("For Your Information") returns "FYI"
#f("Python") returns "P"

def f(name):
    result = ""
    words = name.split() # Dzielimy tekst na listę słów.
    for word in words: # Przechodzimy po kolei przez każde słowo.
        result += word[0] # Pobieramy pierwszą literę słowa i dopisujemy ją do skrótu.
    return result

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))