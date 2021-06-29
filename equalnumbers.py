# Problem 3.A
# Purpose: Practice compound boolean expressions
# Problem Statement:  Given three integers. Determine how many of them are equal to each other. 
# The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third one is different) or 0 (if all numbers are different).

# a b c
# a = b = c : 3
# a = c or b = c or a = c : 2
# else : 0 

num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 == num2 == num3):
   print(3)
elif (num1 == num2 or num2 == num3 or num1 == num3):
   print(2)
else:
   print(0)
   
