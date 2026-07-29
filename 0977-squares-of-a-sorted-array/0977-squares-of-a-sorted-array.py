class Solution(object):
    def sortedSquares(self, nums):
        
        n = len(nums)

        ans = [0]*n

        left=0
        right= n-1

        index = n-1
        
        while left <= right :

            if abs(nums[left]) > abs(nums[right]):
                ans[index] = nums[left]**2
                left += 1
            else:    
                ans[index] = nums[right]**2
                right -= 1

            index -= 1
        return ans       
