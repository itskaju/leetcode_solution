class Solution:
    def majorityElement(self,nums):

        freq = {}
        n = len(nums)

        for num in nums:
            freq[num] = freq.get(num,0)+1

            if freq[num] > n//2:
                return num