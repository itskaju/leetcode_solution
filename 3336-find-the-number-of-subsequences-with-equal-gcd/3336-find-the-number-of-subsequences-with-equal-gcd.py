from math import gcd
from functools import lru_cache

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(i, g1, g2):
            # All numbers processed
            if i == len(nums):
                if g1 == g2 and g1 != 0:
                    return 1
                return 0

            x = nums[i]

            # Option 1: Skip current element
            ans = dp(i + 1, g1, g2)

            # Option 2: Put in first subsequence
            new_g1 = x if g1 == 0 else gcd(g1, x)
            ans += dp(i + 1, new_g1, g2)

            # Option 3: Put in second subsequence
            new_g2 = x if g2 == 0 else gcd(g2, x)
            ans += dp(i + 1, g1, new_g2)

            return ans % MOD

        return dp(0, 0, 0)