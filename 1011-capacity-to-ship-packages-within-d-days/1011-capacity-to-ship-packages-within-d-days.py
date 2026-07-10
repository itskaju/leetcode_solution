class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(capacity):
            days_needed = 1 
            current = 0

            for w in weights:
                if current + w > capacity:

                   days_needed += 1
                   current = 0
                current += w

            return days_needed  <= days

        left = max(weights)
        right = sum(weights)

        while left< right:
            mid = (left + right) // 2 

            if canship(mid):
                right = mid
            else:
                left = mid + 1

        return left                      