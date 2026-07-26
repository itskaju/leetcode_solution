class Solution:
    def dominantIndex(self, nums):
        if len(nums) == 1:
            return 0
        max1 = max(nums)
        idx = nums.index(max1)
        nums_copy = nums[:]
        nums_copy.remove(max1)
        max2 = max(nums_copy)
        if max1 >= 2 * max2:
            return idx
        return -1
