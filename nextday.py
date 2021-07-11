# Given a month (an integer from 1 to 12) and a day in it (an integer from 1 to 31) in the year 2017, print the month and the day of the next day to it.
# Matching: Calculating days in a given month from a given year,

# Planning:
# 1. Get user month number
# 2. Get user date number
# 3. If it's the last day of the month:
  # Increment month
  # Change date to 1
# 4. If it's the last day of the year:
  # Change month to year
  # Change date to 1
# 5. Else
  # Increment date
  
# 1. Get user month number
month = int(input())
# 2. Get user date number
date = int(input())
# 3. If it's the last day of the month:
# Increment month
# Change date to 1
# case february
if (month == 2 and date == 28):
   month += 1
   date = 1
# case april, june, sept, nov
elif (month == 4 or month == 6 or month == 9 or month == 11) and (date == 30):
   month +=1
   date = 1
# case jan, march, may, july, aug, oct
elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and (date == 31):
   month +=1
   date = 1
# case dec 31
elif (month == 12 and date == 31):
   month = 1
   date = 1
# case 
else:
   date += 1
print(month)
print(date)
