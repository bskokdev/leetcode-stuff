class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= M or c < 0 or c >= N:
                return 1
            if grid[r][c] == 0:
                return 1
            if grid[r][c] == 2:
                return 0
            grid[r][c] = 2
            return dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)

        # exactly one island -> just one start node is needed
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    return dfs(r, c)