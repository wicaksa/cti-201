# Problem 3G

# Purpose: Practice compound boolean expressions

# Problem Statement: 
# Chess bishop moves diagonally in any number of squares. 
# Given two different squares of the chessboard, determine whether a bishop can go from the first square to the second one in a single move.

# The program receives four numbers from 1 to 8 each specifying the column and the row number, 
# first two - for the first square, and the last two - for the second square. 
# The program should output YES if a bishop can go from the first square to the second one in a single move or NO otherwise.

# get current location
x1 = int(input())
y1 = int(input())

# get next location
x2 = int(input())
y2 = int(input())

# calculate the differnce between locations for each coordinate 
xdiff = x2 - x1
ydiff = y2 - y1

# if the abs value is equal, then yes
if (abs(xdiff) == abs(ydiff)):
   print("YES")
# if not then no
else:
   print("NO")
