# Given an integer array nums, return an array answer 
# such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

# O(n^2) time complexity
def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = []

    for k in range(len(nums)):
        total = 1

        for i in range(len(nums)):
            if i != k:
                total *= nums[i]

        answer.append(total)

    return answer

# O(n) time complexity
# answer[i] = left product × right product

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n #[1, 1, 1, ...]

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer