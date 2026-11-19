#Products are marked with a special code consisting of 3 digits and afourth control digit. The forth digit is determined by calculating the remainder of dividing the sum of the first three digits by 7. Define a function f(product_code) that returns True if the product code is correct or False otherwise. Sample result:

#f("1082") returns True
#f("2035") returns True
#f("1114") returns False
#f("7071") returns False

def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit(): # Check whether the code has the wrong length or contains a non-digit.
        return False

    total = int(product_code[0]) + int(product_code[1]) + int(product_code[2])  # Convert the first three digits to integers and add them.
    control_digit = total % 7 # Use the remainder after dividing the sum by 7 as the control digit.

    return control_digit == int(product_code[3]) # Return True if the fourth digit matches the control digit (the remainder after dividing the sum of the first three digits by 7), otherwise False.


print(f("1082")) # Print True because (1 + 0 + 8) % 7 is 2.
print(f("2035")) # Print True because (2 + 0 + 3) % 7 is 5.
print(f("1114")) # Print False because (1 + 1 + 1) % 7 is 3, but the last digit is 4.
print(f("7071")) # Print False because (7 + 0 + 7) % 7 is 0, but the last digit is 1.