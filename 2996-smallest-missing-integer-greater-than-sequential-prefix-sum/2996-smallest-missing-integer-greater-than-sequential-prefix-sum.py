class Solution:
    def missingInteger(self, nums):
        n = len(nums)

        # Step 1: find prefix length
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            i += 1

        # Step 2: sum prefix
        prefix_sum = sum(nums[:i])

        # Step 3: find smallest missing >= prefix_sum
        s = set(nums)

        x = prefix_sum
        while x in s:
            x += 1

        return x