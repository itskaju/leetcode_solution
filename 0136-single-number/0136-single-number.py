class Solution:
    def singleNumber(self,nums:List[int]) -> int:
        freq={}

        for num in nums:
            freq[num] = freq.get(num,0) +1

        for key in freq:
            if freq[key] == 1:
                return key
