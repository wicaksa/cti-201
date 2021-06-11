# Problem

# Write a program that takes two upper case letters as input and prints its
# position number in alphabet sequence,
# [A, B, C, .... X, Y, Z, AA, AB, AC, AD .... AX, AY, AZ, ... ZX, ZY, ZZ]

# Question: Convert two uppercase letters into their positional sequences in the alhpahabet
# Input: String containing two uppercase characters
# Output: Int representing their number in the sequence

def letterToNum(letter):
    """
    Converts a capital letter into numerical value. Numerical value is it's
    location sequence in the alphabet.

    example:
    'A' -> 1
    """
    return (ord(letter) - 64)

# Get user input = such as ('AA')
user_input = input() # string

# Convert the letters into numbers
# Convert First letter: string[0]
first_value = letterToNum(user_input[0])

# Convert second letter: string [1]
second_value = letterToNum(user_input[1])

# Convert into final sequence
final_value = (26 * first_value) + second_value

# Show result on console
print(final_value)
