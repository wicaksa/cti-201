# Problem 3I

# Purpose: Practice compound boolean expressions

 
# Problem Statement: 

# Chess knight can move to a square that is two squares away horizontally and one square vertically, or two squares vertically and one square horizontally. 
# The complete move, therefore, looks like the letter L. 
# Given two different squares of the chessboard, determine whether a knight can go from the first square to the second one in a single move.

# The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - f
# or the second square. The program should output YES if a knight can go from the first square to the second one in a single move or NO otherwise.

# get first location
X1 = int(input())
Y1 = int(input())

# get second location 
X2 = int(input())
Y2 = int(input())

# find the difference for each coordinate
xdiff = X2 - X1
ydiff = Y2 - Y1

# if abs value of x == 1 and abs value of y == 2 OR abs x == 2 and abs value of y == 1, YES else NO
if ( (abs(xdiff) == 1 and abs(ydiff) == 2 ) or ( abs(xdiff) == 2 and abs(ydiff) == 1) ):
   print("YES")
else:
   print("NO")
