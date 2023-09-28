class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        def in_bounds(row, col):
            return row >= 0 and row < m and col >= 0 and col < n

        def dfs(row, col, seen):
            if not in_bounds(row, col) or seen[row][col]:
                return
            seen[row][col] = True
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                if in_bounds(n_row, n_col) and heights[n_row][n_col] >= heights[row][col]:
                    dfs(n_row, n_col, seen)

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        res = []
        # Border DFS
        # columns
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
        # rows
        for i in range(n):
            dfs(0, i, pacific)
            dfs(m-1, i, atlantic)
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        return res