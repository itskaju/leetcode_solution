class Solution(object):
    def intersection(self, nums1, nums2):
        
        freq= {}

        for num in nums1:
            freq[num]= 1

        ans = []

        for num in nums2:
            if num in freq and freq[num] == 1:
                ans.append(num)
                freq[num] = 0

        return ans            
        