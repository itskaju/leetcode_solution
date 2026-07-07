class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        lsum = 0
        rsum = sum(nums)

        min_diff = [math.inf, -1]    

        for i in range(1, n+1):
            lsum += nums[i-1]
            rsum -= nums[i-1] 

            lavg = lsum//i
            ravg = 0 if n-i == 0 else rsum//(n-i)

            diff = abs(lavg - ravg)
            if diff < min_diff[0]:
                min_diff[0] = diff
                min_diff[1] = i-1

        return min_diff[1]        
                  