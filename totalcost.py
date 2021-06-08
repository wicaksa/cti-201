# A cupcake costs A dollars and B cents. 
# Determine how many dollars and cents should one pay for N cupcakes. 
# A program gets three numbers: A, B, N. 
# It should print two numbers: total cost in dollars and cents.

import math

# A cupcake costs A dollars and B cents. 
# Determine how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

# Input: A = dollars, B = cents, N = cupcakes 
# Output: print statement dollars cents

# Get the three inputs
# A float
dollars = float(input())

# B float
cents = float(input())
cents = cents/100

# N float
cupcakes = float(input())

# Combine A and B 
price = dollars + cents # float

# Multiply AB * N (total price) 333.33
total_cost = price * cupcakes

# Separate numbers before decimal 333
final_dollar_amount = math.floor(total_cost)

# Separate numbers after decimal 
final_cent_amount = float(total_cost - final_dollar_amount)

# .33 -> 33
final_cent_amount = int(round((final_cent_amount * 100), 2))

# Print to console 
print(f"{final_dollar_amount} {final_cent_amount}")

