#In the TV class, add support for volume adjustment in the range 0 to 10. 
# The initial value of the volume level is 0. Add two methods to increase and decrease the TV volume level by one. 
# Note that you cannot increase or decrease the volume beyond the specified range. 
# Display the current volume level in the show_status() method. 
# Then check the operation of the TV by adjusting and displaying its volume level.

from tv import TV


def main():
    tv = TV()  # Tworzymy telewizor. Początkowo ustawiony jest kanał 1.
    tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "Eurosport"])
    tv.turn_on()

    tv.decrease_volume()  # Próba zejścia poniżej 0.
    tv.show_status()      # TV is on, channel 1 (TVP1), volume 0

    tv.increase_volume()
    tv.show_status()      # TV is on, channel 1 (TVP1), volume 1

    for _ in range(12):
        tv.increase_volume()
    tv.show_status()      # TV is on, channel 1 (TVP1), volume 10

    tv.decrease_volume()
    tv.show_status()      # TV is on, channel 1 (TVP1), volume 9


if __name__ == "__main__":
    main()
