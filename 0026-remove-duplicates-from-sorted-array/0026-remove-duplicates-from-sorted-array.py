class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
            unique = sorted(seen)
        for i in range(len(unique)):
            nums[i] = unique[i]
        return len(unique)        
