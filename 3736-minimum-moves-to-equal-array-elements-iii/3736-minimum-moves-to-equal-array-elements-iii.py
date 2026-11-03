class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val = max(nums)

        ans = 0
        for num in nums:
            ans += max_val - num

        return ans