# Familiarise yourself with methods of visualizing data:
# https://www.w3schools.com/python/matplotlib_intro.asp
# Use matplotlib to draw a line from position (1, 3) to position (8, 10).
# If needed, install matplotlib with: python -m pip install matplotlib

import matplotlib.pyplot as plt


x_points = [1, 8]
y_points = [3, 10]

plt.plot(x_points, y_points)
plt.show()