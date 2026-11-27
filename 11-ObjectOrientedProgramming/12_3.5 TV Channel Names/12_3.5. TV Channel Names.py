#In the TV class, make changes to the show_status() method so that it prints not only the selected channel number but also its name. 
# When the selected channel number exceeds the list of available channels, the channel name is not displayed.

#TV is on, channel 4 (TVN)
#Then, try using the TV. Set at least 7 channels (seven TV stations), change channel numbers a number of times and print TV status every time.

from tv import TV


def main():
    tv = TV()  # Tworzymy nowy telewizor.
    tv.turn_on()
    tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "Eurosport"])
    # Kanał 9 sprawdza przypadek, w którym lista nie zawiera nazwy.
    for number in [1, 4, 7, 9]:
        tv.set_channel(number)
        tv.show_status()
    tv.turn_off()
    tv.show_status()


if __name__ == "__main__":
    main()
