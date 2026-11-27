#In the TV class, add the channels attribute containing a list of available TV channel names (use an array). Initially, the array should be empty (TV not programmed, no available channels). Add set_channels(channels_list) and show_channels() methods in the TV class, which allows you to set channels on the TV and print the list of available channels. Sample list of available channels:

#Channel list:
#1. TVP1
#2. TVP2
#3. Polsat
#4. TVN
#5. Filmbox
#6. Discovery
#Then, try using the TV set:

from tv import TV


def main():
    tv = TV()  # Tworzymy nowy telewizor.
    tv.show_status()
    tv.turn_on()
    tv.show_status()
    tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", end=""])
    tv.show_channels()
    tv.show_status()
    tv.turn_off()


if __name__ == "__main__":
    main()
