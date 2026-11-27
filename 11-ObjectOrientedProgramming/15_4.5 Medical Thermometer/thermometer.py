import random


class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = None  # Brak wyniku przed pierwszym pomiarem.

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure_temperature(self):
        if self.is_on:
            # randint uwzględnia obie granice. Dzielimy dziesiąte części stopnia przez 10.
            self.temperature = random.randint(340, 420) / 10

    def show_temperature(self):
        if not self.is_on or self.temperature is None:
            print("No temperature reading.")
            return

        # Format .1f pokazuje dokładnie jedną cyfrę po kropce.
        message = f"Temperature: {self.temperature:.1f}C"
        if self.temperature >= 37:
            message += " (fever)"
        print(message)

        # Osobny if pozwala wypisać oba ostrzeżenia dla wyniku od 41.0.
        if self.temperature >= 41:
            print("CRITICAL TEMPERATURE!!")
