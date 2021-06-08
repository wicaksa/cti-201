# Purpose: To practice remainder operation.
  
# Problem Statement:Days of week are numbered as: 0 — Sunday, 1 — Monday, 2 — Tuesday, ..., 6 — Saturday. An integer K in the range 1 to 365 is given. 
# Find the number of day of week for K-th day of year provided that in this year January 1 was Thursday.  

# Note: I will solve this problem following UMPIRE process at the end of this section.


# Q. What day of the week is it on the input day?
# I. Int representing the nth day of the year
# O. Int representing the day of the week 

# Brainstorm 
# Th: 1, 8, 15, 22, 29  (4)
# F: 2, 9, 16, 23, 30   (5)
# Sa: 3, 10, 17, 24, 31 (6)
# Sun: 4, 11, 18, 25    (0)
# Mon: 5, 12, 19, 26    (1)
# Tues: 6, 13, 20, 27   (2)
# Wed: 7, 14, 21, 28    (3)

# input days % 7 would give you remainder of days 
# the remainder gives you the day of the week 

# Take the input
day = int(input())

# Find the day of the week
day_of_week = day % 7 

# Convert the day of the week to 0...6 
# Print to console 

# Thursday
if (day_of_week == 1):
   print (4)
# Friday
if (day_of_week == 2):
   print (5)
# Saturday
if (day_of_week == 3):
   print (6)
# Sunday
if (day_of_week == 4):
   print (0)
# Monday
if (day_of_week == 5):
   print (1)
# Tuesday
if (day_of_week == 6):
   print (2)
# Thursday
if (day_of_week == 7):
   print (3)
