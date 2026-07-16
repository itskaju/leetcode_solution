from math import gcd

class Solution:
    def gcdSum(self, nums):
        prefix = []
        mx = 0

        # Step 1: Build prefixGcd
        for x in nums:
            mx = max(mx, x)
            prefix.append(gcd(x, mx))

        # Step 2: Sort
        prefix.sort()

        # Step 3: Pair smallest with largest
        ans = 0
        n = len(prefix)

        for i in range(n // 2):
            ans += gcd(prefix[i], prefix[n - 1 - i])

        return ans