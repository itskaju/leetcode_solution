class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)

        total_xor = 0
        non_zero = False

        for x in nums:
            total_xor ^= x

            if x != 0:
                non_zero = True

        if total_xor != 0:
            return n

        if not non_zero:
            return 0

        return n - 1