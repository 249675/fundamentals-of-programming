# Write a program that draws the graph of f(x) = x^2 - 3.
# Use x values from -100 to 100.

import matplotlib.pyplot as plt


x_values = []
y_values = []

for number in range(-100, 101):
    x_values.append(number)

for number in x_values:
    y_values.append(number ** 2 - 3)

plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()