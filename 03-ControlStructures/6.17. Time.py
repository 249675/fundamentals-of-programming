#Write a program that allows you to convert time in 24-hour format to 12-hour format. The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm

Time = input("Enter time (24-hour format HH:MM ):")
Hour = int(Time[:2])
Minute = Time[-2:]
if Hour >= 13 and Hour <=23:
    Hour -= 12
    print(f'Time in 12-hour format: {Hour}:{Minute} PM')
elif Hour == 12:
    print(f'Time in 12-hour format: 12:{Minute} PM')
elif Hour == 00:
    print(f'Time in 12-hour format: 12:{Minute} AM')    
else:
    print(f'Time in 12-hour format: {Hour}:{Minute} AM')