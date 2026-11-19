# Write a program that, for a given array of real numbers, prints
# the number of elements greater than a value entered from the keyboard.

numbers = [1.5, 8.2, -3.4, 4.0, 6.7]
threshold = float(input("Enter a value: "))
count = 0

for number in numbers:
    if number > threshold:
        count += 1

print("Array:", *numbers)
print("Number of elements greater than the given value:", count)