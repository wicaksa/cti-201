# Problem 3F

# Purpose: Practice compound boolean expressions

# Problem Statement: 
# Chess king moves one square in any direction. Given two different squares of the chessboard, determine whether a king can go from the first square to the second one in a single move.
# The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. 
# The program should output YES if a king can go from the first square to the second one in a single move or NO otherwise.

# Checks to see if the king can make a valid move
# takes in current coordinate and next coordinate
def validMove(sq1, sq2, sq3, sq4):
   sq1diff = sq3 - sq1
   sq2diff = sq4 - sq2
   
   if ( sq1diff in (-1, 0, 1) and sq2diff in (-1, 0, 1) ):
      return "YES"
   else:
      return "NO"

# Get first coordinate
p1s1 = int(input())
p1s2 = int(input())
# Get second coordinate
p2s1 = int(input())
p2s2 = int(input())
# Can only get to second coordinate if first and second value are +1, -1, or 0 away from each coordinate
valid = validMove(p1s1, p1s2, p2s1, p2s2)
print(valid)

