from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):
            day = 1
            load = 0

            for w in weights:
                if load + w > capacity:
                    day += 1
                    load = 0
                load += w

            return day <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left