class Solution(object):
    def zeroFilledSubarray(self, nums):
        streak = 0
        count = 0

        for num in nums:
            if num == 0:
                streak += 1
                count += streak
            else:
                streak = 0
        return count        

        
        