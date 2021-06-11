# Problem
# Given two input numbers,print 'True' if the last least significant bit of the
# two number match and 'False' if they don't.

# Question: Check to see if the last bit of each decimal value equal one another.
# Input: String input that contain two numbers (need to extract) use string split
# Output: Boolean value representing if last bit of the two numbers are the same


# Get user input
user_input = input() # "2 5"

# Split the user input into a list strings to get rid of space
user_input = (user_input.split(" ")) # user_input = ['2', '5']

# Convert first number into binary
num1 = int(user_input[0]) # '2' -> 2
bin1 = bin(num1)

# Convert second number into binary
num2 = int(user_input[1]) # '5' -> 5
bin2 = bin(num2)

# Check the last digit of both numbers to see if they are equal
# Show to console
print(bin1[-1] == bin2[-1])
