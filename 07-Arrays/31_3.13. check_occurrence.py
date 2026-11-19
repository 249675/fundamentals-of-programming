# Define a function occurs(number, array) that returns True if a given
# number is present in an array.
# Check whether the number entered from the keyboard is present
# in the array [15, 38, 7, 23, 14].

def occurs(number, array):
    return number in array


numbers = [15, 38, 7, 23, 14]
number = int(input("Number: "))

print("Array:", *numbers)

if occurs(number, numbers):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")