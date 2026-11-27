#Add the set_channel(new_channel_no) method in the TV class to set the TV channel number. Then try using the TV set.

#Create a TV set
#Show TV status
#Turn TV on
#Show TV status
#Change TV channel to 5
#Show TV status
#Turn TV off
#Show TV status
#In the TV class, add the channels attribute containing a list of available TV channel names (use an array). Initially, the array should be empty (TV not programmed, no available channels). Add set_channels(channels_list) and show_channels() methods in the TV class, which allows you to set channels on the TV and print the list of available channels. Sample list of available channels:



class TV:
    def __init__(self):
        self.is_on = False  # Telewizor zaczyna wyłączony.
        self.channel_no = 1  # Numer kanału liczymy od 1.
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no  # Zapisujemy wybrany kanał.

    def show_status(self):
        # Stan zasilania decyduje, które informacje wypiszemy.
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")
