# The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
# Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

Parking_duration = int(input("Please enter number of hours of parking: "))

if Parking_duration > 6:
    print (f'Parking Duration: {Parking_duration} hours. Please pay 20 PLN')
elif Parking_duration >=3:
    print (f'Parking Duration: {Parking_duration} hours. Please pay 15 PLN')
elif Parking_duration >= 1 and Parking_duration <=2:
    print (f'Parking Duration: {Parking_duration} hours. Please pay 5 PLN')

