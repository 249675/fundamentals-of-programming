#In a separate module, define a function that checks if the number is within the range <x, y>. The function returns a boolean value. Then, create a program and use the function you defined. Sample result:

def in_range (number,x,y):
    if number >= x and number <= y: # Sprawdzamy oba warunki. Liczba może też być równa którejś z granic.
        return True # Zwracamy True, jeśli liczba należy do przedziału.
    else:
        return False