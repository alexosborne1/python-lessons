# Fibonacci Sequence Example
# Jake Malley

"""
Prints out the Fibonacci Sequence, starting at 1, up to a set value.
"""

# Get the maximum value.
maximum_value = int(raw_input("Enter the maximum value:"))

# Start at 1,1
sequence = [1,1]
# Set a value to temporarily store the next term.
next_term = -1
# Print out the first two terms.
print("1\n1")

# Extension: Sum the output. (Set to two as be have started at 1,1)
cumulative_sum = 2

# While the next term is less than the maximum value we set.
while next_term < maximum_value:
    # Generate a new term. (With the last two numbers in the sequence array.)
    next_term = sequence[-2]+sequence[-1]
    # Add the new term to the sequence array.
    sequence.append(next_term)
    # Print it out.
    print(next_term)

    # Add the new term to the sum.
    cumulative_sum = cumulative_sum + next_term

print("============================")
print("Sum:")
print(cumulative_sum)

