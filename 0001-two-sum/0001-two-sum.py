class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = {}  # Dictionary: number -> index

        for i in range(len(nums)):
            first = nums[i]
            sec = target - first

            # If the required complement already exists
            if sec in m:
                return [m[sec], i]

            # Store the current number and its index
            m[first] = i