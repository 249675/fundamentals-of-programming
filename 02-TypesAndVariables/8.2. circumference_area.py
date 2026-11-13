###
# Calculation of circle area and circumference 
#

# determine radius and PI values
radius = int(input("Enter the radius of the circle: "))
pi = 3.14
# calculate area    
area = pi * radius ** 2
# calculate circumference   
circumference = 2 * pi * radius
# print results
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")