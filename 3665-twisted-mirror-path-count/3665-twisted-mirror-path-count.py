class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # down[j]: paths arriving at (i, j) from above
        down = [0] * n
        answer = 0

        for i in range(m):
            right = 0  # paths arriving at (i, j) from the left

            for j in range(n):
                if i == 0 and j == 0:
                    # The start is empty; the robot may choose either direction.
                    right = 1
                    down[j] = 1
                    continue

                from_left = right
                from_above = down[j]

                if grid[i][j] == 1:
                    # Rightward arrivals turn down; downward arrivals turn right.
                    right = from_above % MOD
                    down[j] = from_left % MOD
                else:
                    # At an empty cell, each arriving path can choose either move.
                    ways = (from_left + from_above) % MOD
                    right = ways
                    down[j] = ways

                if i == m - 1 and j == n - 1:
                    answer = (from_left + from_above) % MOD

        return answer