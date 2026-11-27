#In the TV class, add the channel_no attribute indicating the number of the current TV channel displayed by the TV set.
#  Initially, the TV is set to channel 1. Modify the show_status() method so that it also prints the TV channel number,
#  but only if the TV is turned on:

class TV:
    def __init__(self):
        self.is_on = False  # Telewizor zaczyna wyłączony.
        self.channel_no = 1  # Numer kanału liczymy od 1.
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        # Stan zasilania decyduje, które informacje wypiszemy.
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")
