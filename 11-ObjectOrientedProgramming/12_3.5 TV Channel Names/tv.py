#In the TV class, make changes to the show_status() method so that it prints not only the selected channel number but also its name. 
# When the selected channel number exceeds the list of available channels, the channel name is not displayed.

#TV is on, channel 4 (TVN)
#Then, try using the TV. Set at least 7 channels (seven TV stations), change channel numbers a number of times and print TV status every time.

class TV:
    def __init__(self):
        self.is_on = False  # Telewizor zaczyna wyłączony.
        self.channel_no = 1  # Numer kanału liczymy od 1.
        self.channels = []  # Na początku telewizor nie ma zaprogramowanych stacji.
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

    def show_status(self):
        # Stan zasilania decyduje, które informacje wypiszemy.
        if self.is_on:
            status = f"TV is on, channel {self.channel_no}"
            # Po sprawdzeniu zakresu zamieniamy numer kanału na indeks od 0.
            if 1 <= self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no - 1]
                status += f" ({channel_name})"
            print(status)
        else:
            print("TV is off")
