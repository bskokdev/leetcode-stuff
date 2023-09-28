class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        level = -1
        while q:
            level += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dx, dy in dirs:
                    nr, nc = row + dx, col + dy
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1

        return max(level, 0) if fresh == 0 else -1


        