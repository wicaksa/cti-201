# Given five integers, print the least of them.

# create variable to store smallest number
smallNum = int(input())

# create a loop for user input
i = 4
while (i > 0):
   # if input is smaller than current smallest number
   userInput = int(input())
   if (userInput < smallNum):
      # set that number as the smallest number
      smallNum = userInput
   # decrement i
   i -= 1
# print smallest number
print(smallNum)
