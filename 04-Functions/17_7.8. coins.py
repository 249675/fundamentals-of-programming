#The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. Sample result:

#f(23) returns 6
#f(8) returns 3
#f(2) returns 1
#f(0) returns 0


def f(amount_to_pay): # Obliczamy liczbę monet o nominałach 5, 2 i 1.
    coins = amount_to_pay // 5  # Liczymy, ile monet o nominale 5 mieści się w kwocie.
    remaining = amount_to_pay % 5 # Obliczamy, ile zostało do zapłaty po użyciu tych monet.
    result = remaining // 2   # Liczymy, ile monet o nominale 2 mieści się w pozostałej kwocie.
    coins += result  # Dodajemy liczbę monet o nominale 2 do licznika.
    remaining = remaining % 2 # Sprawdzamy, czy po użyciu monet o nominale 2 zostało 0 czy 1.
    coins += remaining # Jeśli zostało 1, doliczamy jedną monetę o nominale 1.
    return coins # Zwracamy łączną liczbę monet.


print(f(23)) 
print(f(8))
print(f(2))
print(f(0))