#The following function calculates the factorial recursively. Try to analyse the function. Do you understand how it works? Then, write a program and use the function to calculate the factorial value for n = 5.

#def factorial(n): 

# 0! = 1, 1! = 1
#    if n==0 or n==1:
#        return 1

# n! = n * (n-1)!
#    if n > 1: # brakowało wcięcia
#     return n * factorial(n - 1) # brakowało wcięcia

#print("==============================================")

def factorial(n): # Define a function that calculates n factorial (n!).
    if n == 0 or n == 1: # Check whether we have reached a base case.
        return 1 # Return 1 and stop the recursion because 0! and 1! both equal 1.

    if n > 1:  # For numbers greater than 1, calculate the factorial recursively.
        return n * factorial(n - 1) # Call the same function with n - 1, then multiply its result by n.


print(factorial(5))