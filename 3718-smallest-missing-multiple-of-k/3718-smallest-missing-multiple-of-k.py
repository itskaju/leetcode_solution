class Solution:
    def missingMultiple(self, nums, k):
        s = set(nums)

        i = 1
        while True:
            val = i * k
            if val not in s:
                return val
            i += 1