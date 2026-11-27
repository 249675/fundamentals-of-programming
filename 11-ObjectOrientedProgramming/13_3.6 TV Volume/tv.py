#In the TV class, add support for volume adjustment in the range 0 to 10. 
# The initial value of the volume level is 0. Add two methods to increase and decrease the TV volume level by one. 
# Note that you cannot increase or decrease the volume beyond the specified range. 
# Display the current volume level in the show_status() method. 
# Then check the operation of the TV by adjusting and displaying its volume level.

class TV:
    def __init__(self):
        self.is_on = False  # Telewizor zaczyna wyłączony.
        self.channel_no = 1  # Numer kanału liczymy od 1.
        self.channels = []  # Na początku telewizor nie ma zaprogramowanych stacji.
        self.volume = 0  # Telewizor zaczyna z głośnością 0.
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no  # Zapisujemy wybrany kanał.

    def set_channels(self, channels_list):
        self.channels = channels_list  # Przypisujemy listę stacji do telewizora.

    def show_channels(self):
        print("Channel list:")
        # Numerujemy stacje tak jak na pilocie, od 1.
        number = 1
        for name in self.channels:
            print(f"{number}. {name}")
            number += 1

    def increase_volume(self):
        if self.volume < 10:  # Na poziomie 10 głośność zostaje bez zmian.
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:  # Na poziomie 0 głośność zostaje bez zmian.
            self.volume -= 1

    def show_status(self):
        # Stan zasilania decyduje, które informacje wypiszemy.
        if self.is_on:
            status = f"TV is on, channel {self.channel_no}"
            # Po sprawdzeniu zakresu zamieniamy numer kanału na indeks od 0.
            if 1 <= self.channel_no <= len(self.channels): # Sprawdzamy, czy numer kanału mieści się w zakresie listy.
                channel_name = self.channels[self.channel_no - 1]   # Odejmujemy 1, ponieważ indeksy listy zaczynają się od 0.
                status += f" ({channel_name})"
            print(f"{status}, volume {self.volume}")
        else:
            print("TV is off")
