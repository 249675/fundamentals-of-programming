###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

Celsius = float(input("Enter temperature in degrees Celsius: ")) # Put temperature in Celsius
Ferenheit = (Celsius * 9/5) + 32 #result of conversion to Ferenheit
Kelvin = Celsius + 273.15 #result of conversion to Kelvin
print(f"Temperature in Celsius: {Celsius}")
print(f"Temperature in Fahrenheit: {Ferenheit}")
print(f"Temperature in Kelvin: {Kelvin}")