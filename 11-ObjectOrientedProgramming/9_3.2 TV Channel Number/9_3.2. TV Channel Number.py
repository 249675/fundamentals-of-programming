#In the TV class, add the channel_no attribute indicating the number of the current TV channel displayed by the TV set.
#  Initially, the TV is set to channel 1. Modify the show_status() method so that it also prints the TV channel number,
#  but only if the TV is turned on:

from tv import TV


def main():
    tv = TV()  # Tworzymy nowy telewizor.
    tv.turn_on()
    tv.show_status()
    tv.turn_off()
    tv.show_status()


if __name__ == "__main__":
    main()
