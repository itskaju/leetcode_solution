class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        
        # Step 1: find pivot
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: swap with next greater
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse right part
        nums[i+1:] = reversed(nums[i+1:])           
        