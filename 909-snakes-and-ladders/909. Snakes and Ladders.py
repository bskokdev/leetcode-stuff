class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def get_coordinates(square: int) -> [int, int]:
            r = (square-1) // n
            c = (square-1) % n
            if r % 2:
                c = n - 1 - c
            return [r, c]

        q = deque([1])
        seen = set()
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(1, 7):
                    next_square = cur + i
                    r, c = get_coordinates(next_square)
                    if board[r][c] != -1:
                        next_square = board[r][c]
                    if next_square == n**2:
                        return level
                    if next_square not in seen:
                        q.append(next_square)
                        seen.add(next_square)
        return -1