class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        if (m+n-1)% 2!=0:
            return False
        memo = set()

        def dfs(i,j, balance):
            if i >= m or j >= n:
                return False
            if grid[i][j] == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
            if i == m-1 and j == n-1:
                return balance == 0
            if (i,j, balance) in memo:
                return False
            memo.add((i,j, balance))

            return dfs(i+1, j, balance) or dfs(i, j+1, balance)
        return dfs(0,0,0)                 
