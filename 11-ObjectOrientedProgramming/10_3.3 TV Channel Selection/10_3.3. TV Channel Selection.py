#Add the set_channel(new_channel_no) method in the TV class to set the TV channel number. Then try using the TV set.

#Create a TV set
#Show TV status
#Turn TV on
#Show TV status
#Change TV channel to 5
#Show TV status
#Turn TV off
#Show TV status


from tv import TV


def main():
    tv = TV()  # Tworzymy nowy telewizor.
    tv.show_status()
    tv.turn_on()
    tv.show_status()
    tv.set_channel(5)
    tv.show_status()
    tv.turn_off()
    tv.show_status()


if __name__ == "__main__":
    main()
