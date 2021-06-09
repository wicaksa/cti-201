# Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).
# For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2 30.

# Input: N the number of minutes that is passed since midnight 
# Output: How many hours and minutes are displayed on the 24h digital clock


# Get user input N (minutes) # 100 min 
user_input = int(input()) # MINUTES

# Calculate how many hours
hours = int(user_input // 60) # 100 // 60 = 1hr

# If hours are over 24 hours, do modulo division 
if (hours > 24):
	hours = hours % 24

# Calculate how many minutes
minutes = int(user_input % 60)

# Show final time on clock 
print(f"{hours} {minutes}")
