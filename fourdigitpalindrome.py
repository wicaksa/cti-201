# Problem 3.7 
# Purpose: Practice compound boolean expressions
# Problem Statement: Let's call an integer a palindrome if it remains the same 
# after reading its digits from right to left. Given a four-digit integer, 
# print "YES" if it's a palindrome and print "NO" otherwise.

# get user input as an integer
userInput = int(input())

# extract ones digit
onesDigit = userInput % 10 

# extract tens digit
tensDigit = (userInput // 10) % 10

# extract hundreds digit
hundredsDigit = (userInput // 100) % 10 

# extract thousands digit
thousandsDigit = (userInput // 1000)

# if first and last are equal and second and third are equal return YES
if ( (onesDigit == thousandsDigit) and (tensDigit == hundredsDigit) ):
   print("YES")
# else return no
else:
   print("NO")
