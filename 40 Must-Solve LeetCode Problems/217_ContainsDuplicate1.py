# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            if i in a:
                return True
            else:
                a.add(i)
        return False

nums = [1,2,3,1]

print("Solution:", Solution().containsDuplicate(nums))