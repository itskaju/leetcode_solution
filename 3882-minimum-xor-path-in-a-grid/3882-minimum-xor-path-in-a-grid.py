class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                prev = set()
                if r > 0:
                    prev.update(dp[r - 1][c])
                if c > 0:
                    prev.update(dp[r][c - 1])

                dp[r][c] = {x ^ grid[r][c] for x in prev}

        return min(dp[m - 1][n - 1])