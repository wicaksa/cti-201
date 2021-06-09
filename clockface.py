# The hour hand of an analog clock turned α degrees since the midnight. 
# Determine and print the angle by which the minute hand turned since the start of the current hour. 
# Input and output in this problems are integers. 

# Understand: Find the angle that is shown by the current time. 
# Input: degrees that the hour hand moved
# Output: degrees that the minute hand moved 

# 360 degrees in a circle
# 1 hour = 30 degrees
# 1 min = 6 degrees

# degree hour hand moved -> hour -> minute -> degree minute hand moved 

# Get input 
input = int(input()) # amount of degrees that hour hand moves 

# Convert degrees to hours passed
hours_passed = (input / 30)

# convert hours to minutes passed
minutes_passed = (hours_passed * 60)

# convert minutes to degrees passed 
# do modulo division because any multiple of 60 % is back at 0 degrees
degrees_passed = int((minutes_passed * 6) % 360)

# show in console 
print(str(degrees_passed))
