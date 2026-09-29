class Solution(object):
    def firstMissingPositive(self, nums):
        s = set(nums)

        i = 1
        while True:
            if i not in s:
                return i
            i += 1    