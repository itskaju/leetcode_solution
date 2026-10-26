class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        answer = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                total = 0
                stack = [(r, c)]
                total += grid[r][c]
                grid[r][c] = 0  # mark visited

                while stack:
                    i, j = stack.pop()

                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > 0:
                            total += grid[ni][nj]
                            grid[ni][nj] = 0
                            stack.append((ni, nj))

                if total % k == 0:
                    answer += 1

        return answer