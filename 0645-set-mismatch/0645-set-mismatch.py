class Solution:
    def findErrorNums(self, arr):
        n = len(arr)
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        repeat = -1
        missing = -1

        for i in range(1, n + 1):
            if freq.get(i, 0) == 2:
                repeat = i
            elif freq.get(i, 0) == 0:
                missing = i

        return [repeat, missing]