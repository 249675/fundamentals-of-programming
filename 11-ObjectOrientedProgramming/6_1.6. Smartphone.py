#Identify at least 3 states and 3 behaviors for your smartphone. Then, for the listed states and behaviors, 
# create a class with attributes and methods. 
# Try to use verbs in method names as they describe activities. 
# Finally, create a smartphone object, call its methods and display object’s properties.

class Phone:
    def __init__(self):
        self.is_on = False  # Telefon startuje wyłączony.
        self.battery_level = 40  # Poziom baterii w procentach.
        self.is_muted = False  # Wyciszenie jest początkowo wyłączone.

    def turn_on(self):
        self.is_on = True

    def charge(self, percent):
        # min ogranicza poziom naładowania do 100 procent.
        self.battery_level = min(self.battery_level + percent, 100)

    def mute(self):
        self.is_muted = True

    def show_status(self):
        print(f"Power on: {self.is_on}")
        print(f"Battery: {self.battery_level}%")
        print(f"Muted: {self.is_muted}")


# Wywołujemy trzy metody zmieniające stan i sprawdzamy efekt.
phone = Phone()
phone.turn_on()
phone.charge(30)
phone.mute()
phone.show_status()
