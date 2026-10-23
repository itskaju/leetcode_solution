from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1

        for i, value in enumerate(nums):
            if value != i:
                k &= value & i

        return max(k, 0)