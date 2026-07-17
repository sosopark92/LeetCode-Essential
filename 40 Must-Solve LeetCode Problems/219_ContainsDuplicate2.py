# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k.

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}

        for i, num in enumerate(nums):
            if num in num_dict and i - num_dict[num] <= k:
                return True
            else:
                num_dict[num] = i
        return False
    
nums = [1,2,3,1,2,3]
k = 2

solution = Solution()
result = solution.containsNearbyDuplicate(nums, k)
print(result)  # Output: False