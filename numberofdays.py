# Problem 3.9
# Problem Statement:  Given a month - an integer from 1 to 12, print the number of days in it in the year 2017.

# Input: An integer representing the month (1-12)
# Output: An integer representing the number of days 

# Get user input and store it as an int 
userInput = int(input())

# If it's 2, return 28
if (userInput == 2):
   print(28)
# If it's 4, 6, 9, 11 print 30
elif (userInput == 4 or userInput == 6 or userInput == 9 or userInput == 11):
   print(30)
# else print 31
else:
   print(31)
