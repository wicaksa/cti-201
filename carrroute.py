import math

# Purpose: Simple arithmetic operations like rounding.
#
# Problem Statement:
# A car can cover a distance of N kilometers per day.
# How many days will it take to cover a route of length M kilometers?
# The program gets two numbers: N and M.

# Question: How many days will it take to cover a route of length M kilometers?
# Input: int N = Rate of travel (N km/ day)
#        int M = Length of route (M km)

# Days travel = (day / N km) * (M km)

# example: N = 10, M = 999
# days traveled = (day/10) * 999 = 999/10 = 99.9 -> round up -> 100

# example: N = 10, M = 1001
# days traveled = (day/10) * 1001 = 100.1 -> round up 101

# Get inputs from user
travel_rate = int(input())
travel_dist = int(input())

# Find number of days traveled -> round up
travel_days = math.ceil((1/travel_rate) * (travel_dist))

# Print value to console
print(travel_days)
