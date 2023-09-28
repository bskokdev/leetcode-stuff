class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque()
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        def dfs(row, col):
            grid[row][col] = 2
            q.append((row, col))
            for dx, dy in dirs:
                nr, nc = row + dx, col + dy
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    dfs(nr, nc)

        def find_first_island():
            for r in range(N):
                for c in range(N):
                    if grid[r][c] == 1:
                        return r, c
        
        first_r, first_c = find_first_island()
        dfs(first_r, first_c)
        res = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dx, dy in dirs:
                    nr, nc = row + dx, col + dy
                    if 0 <= nr < N and 0 <= nc < N:
                        if not grid[nr][nc]:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                        elif grid[nr][nc] == 1:
                            return res
            res += 1
        return -1


        
        
