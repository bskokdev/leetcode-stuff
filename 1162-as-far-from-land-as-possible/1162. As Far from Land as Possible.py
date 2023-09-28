class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        n = len(grid)
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r,c))
        # no water cell
        if len(q) == n ** 2:
            return -1
        # initial node in the queue is grid[row][col] == 1
        # we only want water cells, therefore don't consider this node    
        level = -1
        while q:
            level += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dx, dy in dirs:
                    nr, nc = row + dx, col + dy
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        q.append((nr, nc))
                        grid[nr][nc] = 1
        return level


