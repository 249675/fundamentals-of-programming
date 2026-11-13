###
# A program that prints your height both in cm and in feet and inches.
#
cm = 176
feet = cm // 30.48 # calculate the number of feet
inches = ((cm % 30.48) / 2.54) # calculate the number of inches

print(f'I am {cm}cm tall, i.e. {feet:.0f} feet and {inches:.2f} inches')