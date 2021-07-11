# Write a program that solves a linear equation ax = b in integers. 
# Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise.

# get user inputs for a and b 
a = int(input())
b = int(input())
# case 1: b/a when a = 0 and b = 0  :  many solutions
if (a == 0 and b == 0):
   print("many solutions")
# case 2: b/a when a = 0 and b != 0 :  no solution 
elif (a == 0 and b != 0):
   print("no solution")
# case 3: b/a when a > b : 
else:
   # if result is a float : print no solution
   if (b % a != 0):
      print("no solution")
   # else: print result
   else:
      print(b/a)
