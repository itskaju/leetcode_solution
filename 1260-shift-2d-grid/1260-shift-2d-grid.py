class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                old = i * n + j
                new = (old + k) % (m * n)

                r = new // n
                c = new % n

                ans[r][c] = grid[i][j]

        return ans