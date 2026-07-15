class Solution:
    def findErrorNums(self, arr):
        arr.sort()
        n = len(arr)

        repeat = -1
        missing = 1

        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                repeat = arr[i]
            elif arr[i] > arr[i - 1] + 1:
                missing = arr[i - 1] + 1

        if arr[-1] != n:
            missing = n

        return [repeat, missing]