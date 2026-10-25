class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def flood(r: int, c: int) -> bool:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if grid[r][c] == 1:
                return True

            grid[r][c] = 1  # Mark visited
            return (
                flood(r - 1, c)
                & flood(r + 1, c)
                & flood(r, c - 1)
                & flood(r, c + 1)
            )

        closed = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and flood(r, c):
                    closed += 1

        return closed