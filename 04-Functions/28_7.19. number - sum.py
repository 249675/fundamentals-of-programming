#Define a function f(number) that returns the sum of repeated digits in a number. Sample result:

#f(1027) returns 0
#f(230335) returns 9
#f(513553007) returns 21

def f(number):
    total = 0 # Zaczynamy od sumy równej 0.
    text = str(number) # Zamieniamy liczbę na tekst, żeby sprawdzać cyfry po kolei.
    for char in text: # Przechodzimy przez każdy znak w tekście.
        if text.count(char) > 1: # Liczymy wystąpienia tej cyfry w całym tekście.
            total += int(char) # Gdy cyfra się powtarza, zamieniamy ją na liczbę i dodajemy do sumy.
    return total # Zwracamy obliczoną sumę.

print(f(1027))
print(f(230335))
print(f(513553007))