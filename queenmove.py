# Problem 3H
# Chess queen moves horizontally, vertically or diagonally in any number of squares. 
# Given two different squares of the chessboard, determine whether a queen can 
# go from the first square to the second one in a single move.

# The program receives four numbers from 1 to 8 each specifying the column and 
# the row number, first two - for the first square, and the last two - for the second square. 
# The program should output YES if a queen can go from the first square to the second one in a single move or NO otherwise.

# Queen moves like a bishop 
# Queen moves like a castle 

# Get location 1
x1 = int(input())
y1 = int(input())

# Get location 2
x2 = int(input())
y2 = int(input())

# Find the difference between coordinates 
xdiff = x2 - x1
ydiff = y2 - y1

# If abs value if difference is equal or x coordinates are the same or y coordinates are the same then YES 
if ( (abs(xdiff) == abs(ydiff)) or (x2 == x1) or (y2 == y1) ):
    print("YES")
# Else false
else:
    print("NO")
