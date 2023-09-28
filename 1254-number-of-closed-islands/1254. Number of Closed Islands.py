class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        def dfs(row, col):
            grid[row][col] = 2
            for dx, dy in dirs:
                nr, nc = row + dx, col + dy
                if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == 0:
                    dfs(nr, nc)

        # 1st and last row
        for i in range(N):
            if grid[0][i] == 0:
                dfs(0, i)
            if grid[M-1][i] == 0:
                dfs(M-1, i)

        # 1st and last col
        for i in range(M):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][N-1] == 0:
                dfs(i, N-1)
        res = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 2 or grid[r][c] == 1:
                    continue
                if grid[r][c] == 0:
                    res += 1
                    dfs(r, c)
        return res
