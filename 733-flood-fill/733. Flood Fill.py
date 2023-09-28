class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        q = deque([(sr, sc)])
        prev_color = image[sr][sc]
        if prev_color == color:
            return image
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == prev_color:
                    q.append((nr, nc))
        return image

