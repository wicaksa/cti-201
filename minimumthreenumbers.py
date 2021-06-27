# Problem 3.8
# Purpose: Practice compound boolean expressions
# Problem Statement: Given three integers, print the least of them.
 
# create a counter
counter = 2

# create a smallest digit variable
smallestDigit = int(input())

# check user inputs to see if it's smaller than current smallest digit
while (counter > 0):
   userInput = int(input())
   if (userInput < smallestDigit):
      smallestDigit = userInput
   counter = counter -1 
#print smallest digit
print(smallestDigit)
