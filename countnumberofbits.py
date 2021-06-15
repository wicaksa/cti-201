# Problem Statement:
# Given five input numbers, a, b, c, d and n, print out the number of 1 bits at
# the nth least significant bit position in all four numbers a, b, c, d.

# Question: Count the number of 1s in the Nth bit of each input.
# Input : 5 integers
# Output: Integer

# Get user input for a - d, then n
user_input = input() # '2 3 4 5 6'

# Split the user input string into a list
user_input = user_input.split()

# separate each entry and store them into variables
a = int(user_input[0])
b = int(user_input[1])
c = int(user_input[2])
d = int(user_input[3])
n = int(user_input[4])
print(f"n = {n}")

# Remove the nth significant bits
a = a >> n
print(f"a = {a}")
b = b >> n
print(f"b = {b}")
c = c >> n
print(f"c = {c}")
d = d >> n
print(f"d = {d}")

## Get the last digit
# Convert to binary -> string
bina = format(a,"b")
print(f"bina = {bina}")
binb = format(b,"b")
print(f"binb = {binb}")
binc = format(c,"b")
print(f"binc = {binc}")
bind = format(d,"b")
print(f"bind = {bind}")

list = [bina, binb, binc, bind]

count = 0
for item in list:
    if (item[-1] == '1'):
        count += 1

print(count)
