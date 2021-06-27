# Purpose: Practice compound boolean expressions
# Problem Statement: Given a three-digit integer X consisting of three different digits, 
# print "YES" if its three digits are going in an ascending order from left to right and print "NO" otherwise.

# get user input
userInput = int(input())

# get one's digit
onesDigit = userInput % 10

# get tens digits
tensDigit = (userInput // 10) % 10

# get hundreds digit
hundredsDigit = (userInput // 100)

# if hundreds < tens < ones return YES else return NO
if (hundredsDigit < tensDigit < onesDigit):
   print("YES")
else:
   print("NO")
