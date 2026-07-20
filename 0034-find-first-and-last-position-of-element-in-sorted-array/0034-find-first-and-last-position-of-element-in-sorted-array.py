from typing import List

class Solution:

    def firstOccurrence(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                ans = mid
                right = mid - 1      # Search left half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def lastOccurrence(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                ans = mid
                left = mid + 1       # Search right half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def searchRange(self, arr: List[int], target: int) -> List[int]:
        first = self.firstOccurrence(arr, target)
        last = self.lastOccurrence(arr, target)

        return [first, last]