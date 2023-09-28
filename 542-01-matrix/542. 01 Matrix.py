class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        res = [[-1] * n for _ in range(m)]
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                    res[r][c] = 0
                
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dx, dy in dirs:
                    nr, nc = row + dx, col + dy
                    if 0 <= nr < m and 0 <= nc < n and res[nr][nc] == -1:
                        q.append((nr, nc))
                        res[nr][nc] = level
        return res