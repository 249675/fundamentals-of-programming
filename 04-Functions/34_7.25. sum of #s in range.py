#Define the function f(x,y), which returns the sum of numbers in the range <x,y> that are completely divisible by 2 and 3 and not divisible by 4. Sample result:

#f(1,20) returns 24
#f(10,30) returns 48

def f(x, y):
    total = 0

    for number in range(x, y + 1): # Loop through all integers from x to y, including y.
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0: # Check that the number is divisible by both 2 and 3 and not divisible by 4.
            total += number # Add the number to the running sum.


    return total


print(f(1, 20)) # Print 24 (6 + 18)
print(f(10, 30)) # Print 48 (18 + 30).