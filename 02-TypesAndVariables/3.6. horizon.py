#The distance to the horizon depends on the height of the observer above the ground. The higher you are, the farther away the horizon is. For most situations, you can use the following formula:
#d = 3.57 × √h

import math

h = input("Enter height in meters: ")
h = float(h)
d = 3.57 * math.sqrt(h)
print("The distance to the horizon is: ", d, "km")
