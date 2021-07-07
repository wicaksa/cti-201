# Problem 3E
# Purpose: Practice compound boolean expressions

# Problem Statement: 
# Given two squares of a chessboard. If they are painted in the same color, print YES, otherwise print NO.
# The program receives four integers from 1 to 8, each specifying the column and row number, first two - for the first square, and then the last two - for the second square.

# function to check color
def checkcolor(s1, s2):
   if (s1 % 2 == 0 and s2 % 2 == 0) or (s1 % 2 != 0 and s2 % 2 != 0):
      return "black"
   else:
      return "white"

# Get user inputs 
# Piece1
p1s1 = int(input())
p1s2 = int(input())
# piece 2
p2s1 = int(input())
p2s2 = int(input())

# Check color of first piece
p1color = checkcolor(p1s1, p1s2)
# Check color of second piece
p2color = checkcolor(p2s1, p2s2)
# Check if they match 
if (p1color == p2color):
   print("YES")
else:
   print("NO")
