# Purpose: To practice remainder and integer division operations.

# Problem Statement:

# A school decided to replace the desks in three classrooms.
# Each desk sits two students.
# Given the number of students in each class,
# print the smallest possible number of desks that can be purchased.

# The program should read three integers: the number of students in each of the
# three classes, a, b and c respectively.

# For example, in the first test there are three groups.
# The first group has 20 students and thus needs 10 desks.
# The second group has 21 students, so they can get by with no fewer
# than 11 desks. 11 desks is also enough for the third group of 22 students.
# So we need 32 desks in total.

# Question: Find the smallest number of desks that can be bought given number of students.
# Input : # integers representing number of students in each class
# Output: # integer representing smallest number of desks that can be bough
# each desk sits 2 people

# example a = 20 b = 21 c = 22
# a : 10 desks, b = 11 (round up), c = 11

# example a = 21 b = 23 c = 25
# a = 11 (round up), b = 12(round up) c = 13 (round up)

# Get inputs from the user and sum it up
input_amount = 3
sum_students = 0

while (input_amount > 0): 
    user_input = int(input())
    # If the input is odd, add 1
    if (user_input % 2 != 0 ):
        user_input += 1
    sum_students = sum_students + user_input 
    input_amount -= 1
    
# Calculate the number of desks each classroom needs 
desks_needed = sum_students / 2

# Print total number of desks needed 
print(desks_needed)
