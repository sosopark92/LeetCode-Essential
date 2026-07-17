# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        sorted_nums = sorted(
            num_dict,
            key=num_dict.get,
            reverse=True
        )

        return sorted_nums[:k]


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}

#         for num in nums:
#             count[num] = count.get(num, 0) + 1

#         return sorted(count, key=count.get, reverse=True)[:k]

nums = [1,1,1,2,2,3]
k = 2
solution = Solution()
result = solution.topKFrequent(nums, k)
print(result)