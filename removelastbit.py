# Problem
# Given two input numbers, print out the two numbers with their binary value
# shifted to the right by 1 bit.

# Input : A string containing two numbers
# Output: A string containing two numbers that was a result of the input bit shifted to the right

# Get user input
user_input = input()

# Split the string into a list
input_list = user_input.split(" ")

# Get Value 1
num1 = int(input_list[0])

# Get Value 2
num2 = int(input_list[1])

# Shift Value 1 (use >>)
num1_new = num1 >> 1

# Shift Value 2
num2_new = num2 >> 1

# Print their values (use , )
print(str(num1_new), str(num2_new))
