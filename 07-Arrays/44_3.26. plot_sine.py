# Write a program that draws y = sin(x) for angles from 0 to 360 degrees.

import math

import matplotlib.pyplot as plt


angles = []
sine_values = []

for angle in range(361):
    angles.append(angle)
    sine_values.append(math.sin(math.radians(angle)))

plt.plot(angles, sine_values)
plt.xlabel("Angle (degrees)")
plt.ylabel("sin(x)")
plt.grid()
plt.show()