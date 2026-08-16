class Solution:
    def findInMountainArray(self, target, mountain_arr):

        n = mountain_arr.length()

        # 1. Find peak
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2

            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid

        peak = low

        # 2. Search increasing side
        low, high = 0, peak

        while low <= high:
            mid = (low + high) // 2

            if mountain_arr.get(mid) == target:
                return mid

            if mountain_arr.get(mid) < target:
                low = mid + 1
            else:
                high = mid - 1

        # 3. Search decreasing side
        low, high = peak + 1, n - 1

        while low <= high:
            mid = (low + high) // 2

            if mountain_arr.get(mid) == target:
                return mid

            if mountain_arr.get(mid) > target:
                low = mid + 1
            else:
                high = mid - 1

        return -1