class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        def in_bounds(row, col):
            return row >= 0 and row < m and col >= 0 and col < n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur = 0
                    q = deque([(i, j)])
                    grid[i][j] = 0
                    while q:
                        row, col = q.popleft()
                        cur += 1
                        for dx, dy in directions:
                            r, c = row + dx, col + dy
                            if in_bounds(r,c) and grid[r][c] == 1:
                                q.append((r,c))
                                grid[r][c] = 0
                    res = max(cur, res)
        return res
        
                
