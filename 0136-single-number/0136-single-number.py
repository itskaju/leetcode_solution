class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        result = 0

        for num in arr:
            result ^= num

        return result
        