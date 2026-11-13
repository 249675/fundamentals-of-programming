###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time #import

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0: #dopóki cuntdown jest wiekesze od zera to leci
    if countdown == 5: #robimy słownie dla 5 ostatnich liczb
        print("five")
    elif countdown == 4:
        print("four")
    elif countdown == 3:
        print("three")
    elif countdown == 2:
        print("two")
    elif countdown == 1:
        print("one")
    else:
        print(countdown) #drukujemy liczby jak lecą w dół
    countdown -= 1 # odejmujemy 1 od wpisaneg countdowna
    time.sleep(1)  # Wait for 1 second #To odmierza 1 sekunde, skok co 1 sekunda, dlatego tyle schodzi
    

print("Time's up!") # while zostanie juz nie do spełnienia, tj dolecimy do 0 wiec warunek countdonw > 0 jest niespełniony