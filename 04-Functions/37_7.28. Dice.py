#The sequence of digits contains the number of points rolled with a dice. Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. Sample result:

#f("5233165554211") returns 5
#f("2133") returns 3

def f(dice): # Take a string of dice rolls, with one character per roll.
    longest = 0 # Store the length of the longest streak found so far.
    count = 0 # Store the length of the current streak.
    previous = "" # Start with an empty string because there is no previous roll yet.
    result = 0 # Store the die value that produced the longest streak.

    for char in dice: # Go through the rolls one at a time.
        if char == previous:  # Check whether this roll matches the previous roll.
            count += 1 # Extend the current streak by one.
        else:
            count = 1 # Count the current roll as the first roll in the new streak.
            previous = char  # Remember the current value for the next comparison.

        if count > longest: # Check whether the current streak is longer than the best one so far.
            longest = count # Save the new longest streak length.
            result = int(char)  # Convert the die value to an integer and save it.

    return result # Return the die value that produced the longest streak.


print(f("5233165554211")) # Print 5 because 555 is the longest streak.
print(f("2133")) # Print 3 because 33 is the longest streak.