#Define a function sum_natural(n) that for the given natural number n calculates the sum of all natural numbers between 1 and n. Apply recursion. Then, create a program that calculates the sum of natural numbers in the range <1,10>.

def sum_natural(n): # Define a function that adds the numbers from 1 to n.
    if n == 0: # Check whether we have reached the base case.
        return 0 # Stop the recursion and return 0.

    return n + sum_natural(n - 1) # Add n to the sum of the numbers from 1 to n - 1.


print(sum_natural(10))