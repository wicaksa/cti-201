import math.random

# Problem Statement:
# Given a year (as a positive integer), find the respective number of the century.
# Note that, for example, 20th century began with the year 1901.

# 2001 - 2100 = 21st century
# 1901 - 2000 - 20th century
# 1801 - 1900 - 19th century
# 1701 - 1800 - 18th century

# Get user input
year_input = int(input())

# Divide input by 100 then round up
century = math.ceil(year_input / 100)

# Print to console
print(century)
