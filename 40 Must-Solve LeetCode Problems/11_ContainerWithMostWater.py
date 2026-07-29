# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0 
        right = len(height) - 1
        best = 0

        while left < right:
            h = min(height[left], height[right])
            best = max(best, h * (right - left))

            # move the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best