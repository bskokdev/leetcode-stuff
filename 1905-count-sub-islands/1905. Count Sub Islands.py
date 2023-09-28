class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        M, N = len(grid1), len(grid1[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        res = 0
        for r in range(M):
            for c in range(N):
                if grid2[r][c] == 0:
                    continue
                is_valid = True
                q = deque()
                q.append((r, c))
                grid2[r][c] = 0
                while q:
                    row, col = q.popleft()
                    if grid1[row][col] == 0:
                        is_valid = False
                    for dx, dy in dirs:
                        nr, nc = row + dx, col + dy
                        if 0 <= nr < M and 0 <= nc < N and grid2[nr][nc] == 1:
                            q.append((nr, nc))
                            grid2[nr][nc] = 0
                if is_valid:
                    res += 1
        return res
                        
