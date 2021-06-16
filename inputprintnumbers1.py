# Problem Statement: Write a program that takes in the user's name, which is taken
# in as input in all lower-case characters. If the least significant bit of the
# ten's place digit of the ASCII representation of the last character of
# the name matches with the least significant bit of the one's place digit of
# the ASCII representation of the last character,
# print "Lsb matches: <tens lsb> <ones lsb>, otherwise print "
# Lsb does not match: <tens lsb> <ones lsb>".

# Input: A string of lowercase letters
# Output: string that tells user if lsb matches
# Question: Compare one's place LSB and tens place LSB to see if they match

# Get user input # anita
inputStr = input()

# Get the last character of the name 'a'
lastChar = inputStr[-1]

# Get the ASCII representation of the letter (int) # 97
lastCharASCII = ord(lastChar)

# Get 10's place value (int) # 9
tensVal = (lastCharASCII % 100) // (10)

# Get 1's place value (int) # 7
onesVal = lastCharASCII % 10

# Get 10's place Binary (int) '1001'
tensBin = format(tensVal, 'b')

# Get 1's place Binary (int) # '0111'
onesBin = format(onesVal, 'b')

# Compare LSB of binary values (Boolean)
sameLSB = (tensBin[-1] == onesBin[-1])

# Print result
if (sameLSB):
    print(f"Lsb matches: {tensBin[-1]} {onesBin[-1]}")
else:
    print(f"Lsb does not match: {tensBin[-1]} {onesBin[-1]}")
