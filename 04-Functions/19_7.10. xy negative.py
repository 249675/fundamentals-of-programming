#Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. Sample result:

#f(-7,8) returns 3
#f(-1,11) returns 0

def f(x,y):
    count = 0
    for number in range(x, y+1): # Sprawdzamy kolejne liczby od x do y włącznie.
        if number < 0 and number % 2 == 0: # Sprawdzamy, czy liczba jest ujemna i dzieli się przez 2 bez reszty.
            count += 1 # Jeśli oba warunki są spełnione, zwiększamy licznik o 1.
    return count

print (f(-7,8))  # Wyświetlamy 3, bo warunek spełniają -6, -4 i -2.
print (f(-1,11))
