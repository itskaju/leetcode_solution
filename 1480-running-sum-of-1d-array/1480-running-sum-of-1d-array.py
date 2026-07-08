class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        psa = []
        psa.append(nums[0])

        for i in range(1, len(nums)) :
            psa.append(nums[i] + psa[i-1]) 

        return psa       
