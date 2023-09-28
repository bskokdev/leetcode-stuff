class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        return res

        
        