#The converters.py file defines two functions for converting length units (cm-->m and m-->cm). The test_converters.py file uses these functions to convert values.

#Define the following functions in the converters.py file that allow you to:

#convert centimeters to inches
#convert feet and inches to centimeters
#Then complete the main program to test the added functions.

def m_to_cm(n): # Przyjmujemy długość w metrach.
    return n*100

def cm_to_m(n): # Przyjmujemy długość w centymetrach.
    return n/100

def cm_to_inches(n): # Przyjmujemy długość w centymetrach.
    return n/2.54

def feet_inches_to_cm(feet,inches): # Przyjmujemy liczbę stóp i cali.
    return feet*30.48 + inches*2.54 

if __name__ == "__main__":  # Uruchamiamy poniższe testy tylko wtedy, gdy uruchomimy ten plik bezpośrednio.
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'2 cm = {cm_to_inches(2):.2f}inches')
    print(f'1 foot + 1 inch = {feet_inches_to_cm(1,1):.2f} cm')