# Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
# The rules in the Gregorian calendar are as follows:

# a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
# a year is always a leap year if its number is exactly divisible by 400

# Warning. The words LEAP and COMMON should be printed all caps.

# 1. Matching: if/else loops, modulo division to find the remainder
# 2. Planning:
   # 1. Take Input and Store it in a variable
   # 2. Leap Year Condition: if (input % 4 == 0 AND input % 100 != 0 print LEAP ) or (input % 400 == 0)
   # 3. Common Year Condition: Else print COMMON
   
inputYear = int(input())
if (inputYear % 4 == 0 and inputYear % 100 != 0) or (inputYear % 400 == 0):
   print("LEAP")
else:
   print("COMMON")
