# Problem 3N

# Problem Statement:

# Given integer coordinates of three vertices of a rectangle whose sides are parallel to coordinate axes, find the coordinates of the fourth vertex of the rectangle. 
# Example input #1

# get the 3 coordinates 
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

# show x possibilities
if (x1 == x2):
   print(x3)
elif (x1 == x3):
   print(x2)
else:
   print(x1)
   
# show y possibilities
if (y1 == y2):
   print(y3)
elif (y1 == y3):
   print(y2)
else:
   print(y1)
