#Define a function power(x, n) that calculates xn. Apply recursion. Then, calculate 5^3.

#Tip: xn = x * xn-1

def power(x, n):  # Define a function that raises x to the power of n.
    if n == 0: # Check whether the exponent has reached zero.
        return 1 # Stop the recursion and return 1.

    return x * power(x, n - 1) # Multiply x by the result of raising x to the power of n - 1.


print(power(5, 3))

#power(5, 3)
#5 * power(5, 2)
# 5 * (5 * power(5, 1))
# 5 * (5 * (5 * power(5, 0)))
# 5 * (5 * (5 * 1))
# 5 * (5 * 5)
# 5 * 25
# 125