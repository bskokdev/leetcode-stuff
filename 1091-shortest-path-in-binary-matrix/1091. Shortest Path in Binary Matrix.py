class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N-1][N-1]:
            return -1
        # row, col, distance
        q = deque([(0,0,1)])
        seen = set()
        seen.add((0,0))
        directions = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,1], [1,-1], [-1,-1]]
        while q:
            r, c, dist = q.popleft()
            if r == c == N-1:
                return dist
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in seen and grid[nr][nc] == 0:
                    q.append((nr, nc, dist+1))
                    seen.add((nr, nc))
        return -1
