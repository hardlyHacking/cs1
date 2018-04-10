# arithmetic_series.py
# Solution to CS 1 Short Assignment 5 by THC.
# Has a function that sums the integers from 1 through n and checks
# that the sum agrees with the formula n * (n+1) / 2.

# Function to check the sum of 1 through n against the formula.
# Returns a boolean indicating whether the sum equals the result
# from the formula.
def check_the_sum(n):
    total = 0           # running sum
    for number in range(1, n+1):
        total = total + number  # update the sum
        
    # Return a boolean indicating whether the sum equals the formula result.
    return total == n * (n+1) / 2

# Repeatedly get a number from the user, and call check_the_sum on
# that number.  Print the result of each call to the console.
# Stop when the number entered is negative.
n = 1       # initialize so that the loop iterates
while n > 0:
    n = int(raw_input("Enter a number: "))
    if n > 0:
        if check_the_sum(n):
            print n, "checks out OK."
        else:
            print n, "does not check out OK"
