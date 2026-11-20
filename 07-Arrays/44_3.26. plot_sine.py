# Write a program that draws y = sin(x) for angles from 0 to 360 degrees.

import math # Importujemy funkcje do przeliczania kątów i obliczania sinusa.

import matplotlib.pyplot as plt # Importujemy moduł do rysowania wykresów.


angles = [] # Lista kątów w stopniach.
sine_values = [] # Lista wartości sinusa dla tych kątów.

for angle in range(361): # Bierzemy kolejne kąty od 0° do 360° włącznie
    angles = angles + [angle]  # Dopisujemy kąt w stopniach do listy.
    radians = math.radians(angle)  # Zamieniamy stopnie na radiany, których oczekuje math.sin().
    sine = math.sin(radians)  # Obliczamy sinus kąta.
    sine_values = sine_values + [sine]  # Dopisujemy wynik do listy wartości sinusa.


plt.plot(angles, sine_values)  # Łączymy każdy kąt z odpowiadającą mu wartością sinusa.
plt.xlabel("Angle (degrees)")  # Podpisujemy oś poziomą, na której są kąty w stopniach.
plt.ylabel("sin(x)")  # Podpisujemy oś pionową, na której są wartości sinusa.
plt.grid()  # Włączamy siatkę.
plt.show()  # Wyświetlamy wykres.