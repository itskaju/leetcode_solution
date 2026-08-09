class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix sum
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0

            # can take all
            if 2 * M >= n - i:
                return suffix[i]

            best = 0

            for X in range(1, 2 * M + 1):
                best = max(best, suffix[i] - dp(i + X, max(M, X)))

            return best

        return dp(0, 1)