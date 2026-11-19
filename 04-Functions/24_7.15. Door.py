# device in a door registers people entering and leaving a room.The + sign means a person entering a room and the -- sign a person leaving a room. Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise. Sample result:

#f("+-+++-+---") returns True
#f("+-+-+-+-") returns False
#f("+-++-+--") returns False
#f("+-++-++-+---") returns True

def f(detector):
    people = 0
    for char in (detector): # Odczytujemy po kolei znaki z detektora.
        if char == "+": # Plus oznacza, że ktoś wszedł.
            people +=1 # Zwiększamy liczbę osób o 1.
        elif char == "-":  # Minus oznacza, że ktoś wyszedł.
            people -=1# Zmniejszamy liczbę osób o 1.

        if people >= 3:  # Po każdym znaku sprawdzamy, ile osób jest w środku.
            return True   # Gdy licznik osiągnie 3, od razu kończymy funkcję.
    return False # Po sprawdzeniu całego zapisu zwracamy False, jeśli licznik ani razu nie osiągnął 3.

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---") )