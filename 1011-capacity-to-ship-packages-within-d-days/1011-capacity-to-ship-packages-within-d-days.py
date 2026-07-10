from typing import List

class Solution:

    def numberOfDays(self, shipWeight: int, arr: List[int]) -> int:
        day = 1
        packageWeight = 0

        for weight in arr:
            packageWeight += weight

            if packageWeight > shipWeight:
                day += 1
                packageWeight = weight

        return day

    def binarySearch(self, minWeight: int, maxWeight: int, arr: List[int], days: int) -> int:
        l = minWeight
        r = maxWeight
        minCapacity = float('inf')

        while l <= r:
            mid = l + (r - l) // 2

            tempDay = self.numberOfDays(mid, arr)

            if tempDay <= days:
                minCapacity = min(minCapacity, mid)
                r = mid - 1
            else:
                l = mid + 1

        return minCapacity

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        minWeightOfShip = max(weights)
        maxWeightOfShip = sum(weights)

        return self.binarySearch(minWeightOfShip, maxWeightOfShip, weights, days)