# Write a program that calculates the volume and surface area of ​​a cuboid with sides a, b, and c. Then, check the program for the following data:
# 
a = input('Enter a: ')
a= int(a)
b = input('Enter b: ')
b= int(b)
c = input('Enter c: ')
c= int(c)

cuboid_volume = a*b*c #volume
cuboid_surface_area = 2*(a*b + a*c + b*c) #surface area

print(f'The volume of a cuboid with sides {a}, {b}, {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, {c}  is {cuboid_surface_area}')


