#Define a function f(text) that returns the given text with all characters separated by a dash sign. Example:

#f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
#f("UE") returns "U-E"
#f("x") returns "x"
#f("") returns ""

def f(text):  # Define a function that takes a string.
    result = ""  # Start with an empty string.

    for i in range(len(text)): # Loop through the indices of the string, starting at 0.
        if i > 0: # Check whether we are past the first character.
            result += "-" # Add a dash before the current character.
        result += text[i] # Add the character at index i.

    return result # Return the completed string.


print(f("University"))  # Print U-n-i-v-e-r-s-i-t-y.
print(f("UE")) # Print U-E.
print(f("x")) # Print x, since there is only one character.
print(f("")) # Print a blank line, since the loop has no characters to process.