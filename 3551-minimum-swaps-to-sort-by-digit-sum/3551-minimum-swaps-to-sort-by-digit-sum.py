
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digit_sum(x):
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total

        arr = sorted((digit_sum(x), x, i) for i, x in enumerate(nums))

        swaps = 0
        visited = [False] * n

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            if cycle_size > 0:
                swaps += cycle_size - 1

        return swaps

