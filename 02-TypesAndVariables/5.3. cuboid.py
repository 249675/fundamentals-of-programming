###
# A program to calculate the volume and surface area of ​​a cube.
# 
a = input('Enter a: ')
a= int(a)
b = input('Enter b: ')
b= int(b)
c = input('Enter c: ')
c= int(c)

cuboid_volume = a*b*c
cuboid_surface_area = 2*(a*b + a*c + b*c)

print(f'The volume of a cuboid with sides {a}, {b}, {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, {c}  is {cuboid_surface_area}')


