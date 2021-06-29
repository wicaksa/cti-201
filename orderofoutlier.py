# Problem 3.B
# Purpose: Practice compound boolean expressions
# Problem Statement:  Given three integers, in which two are equal to each other and the third one is different. 
#                     Print the order number of this different one - 1, 2 or 3.

# Get the three inputs 
num1 = int(input())
num2 = int(input())
num3 = int(input())

# a b c
# a = b : print 3
# a = c : print 2
# b = c : print 1

if (num1 == num2):
   print(3)
elif (num1 == num3):
   print(2)
else: # (num2 == num3):
   print(1)
