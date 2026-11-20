# Write a program that draws the graph of f(x) = x^2 - 3.
# Use x values from -100 to 100.

import matplotlib.pyplot as plt # Importujemy moduł do rysowania wykresów.


x_values = []
y_values = []

for number in range(-100, 101): # Bierzemy kolejne liczby całkowite od -100 do 100.
     x_values = x_values + [number]  # Dopisujemy bieżącą liczbę do listy x.

for number in x_values:
    y = number ** 2 - 3  # Podnosimy x do kwadratu i odejmujemy 3.
    y_values = y_values + [y]  # Dopisujemy wynik do listy y.

plt.plot(x_values, y_values)  # Łączymy punkty (x, y) w kolejności, w której są na listach.
plt.xlabel("x")  # Podpisujemy oś poziomą.
plt.ylabel("f(x)")  # Podpisujemy oś pionową.
plt.grid()  # Włączamy siatkę.
plt.show()  # Wyświetlamy wykres.