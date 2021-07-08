# Problem 268

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # calclate length of nums
        length = len(nums)
   
        # Initialize an empty list (stores what numbers we have seen)
        trackerList = [0] * length
   
        # Iterate thru original list
        for i in range(0, length):
            # place element to empty list that corresponds to the index
            valueInt = nums[i]
            # edge case so it doesn't go out of bounds
            if valueInt != length:
                 trackerList[valueInt] += 1
                    
        # iterate thru second list
        for j in range(0, length):
        # if index element is 0, return index
            if trackerList[j] == 0: 
                return j

        # edge case for end (return length)
        return len(trackerList)
