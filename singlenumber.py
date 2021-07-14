# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(self, nums: List[int]) -> int:
        # sort the list 
        nums.sort()

        # length of input
        l = len(nums)

        # check two numbers at a time from index 0 to len-1
        for i in range (0, l-1, 2):
            n1 = nums[i]
            n2 = nums[i+1]
            # if they don't equal, return the first number
            if (n1 != n2):
                return (n1)
        
        # edge: return the last number 
        return (nums[l-1])
