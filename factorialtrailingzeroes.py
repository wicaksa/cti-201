class Solution:
    def trailingZeroes(self, n: int) -> int:
        # see how many fives go into the input n 
        # input : int n 
        # output: int number of trailing zeros 
        
        # 5/5 = 1
        # 10/5 = 2
        # 15/5 = 3
        # 25 / 5 = 5 + 5 // 5 = 1 because 25/ 5 = 5, you can still divide 5 by 5 to give you 1 
        # 30 / 5 = 6 + 6 // 5 = 1
        
        # traling zero counter = 0 
        
        # while the input can be divisible by 5 :
        #     divide input by 5 
        #     add up total trailing zeros

        # return trailing zeros

        trailingZeros = 0

        while (n // 5 > 0):
            n = n // 5
            trailingZeros += n

        return trailingZeros
