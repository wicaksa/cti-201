# Problem 3D 

# Problem Statement: 
# Given a square of a chessboard. If it's a black square, print YES, otherwise print NO.
# The program receives two integers from 1 to 8 specifying the column and row number of the square.

# Black Square: 1,1 1,3 1,5, 1,7 | 2,2 2,4 2,6 2,8 | (odd odd) (even even)
# White Square: 1,2 1,4 1,6  1,8 | 2,1 2,3 2,5 2,7 | (odd even)(even odd)

# If the two inputs are odd or even, it's black --> YES
# if the two inputs are (odd even) or (even odd), it's white --> NO

square1 = int(input())
square2 = int(input())

# Check black
if (square1 % 2 == 0 and square2 % 2 == 0) or (square1 % 2 != 0 and square2 % 2 != 0):
   print("YES")
# Check white
else:
   print("NO")
