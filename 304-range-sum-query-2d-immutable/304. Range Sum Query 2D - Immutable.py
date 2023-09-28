class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # compute 2d prefix sum
        m, n = len(matrix), len(matrix[0])
        self.p_sum = [[0] * (n+1) for _ in range(m+1)]
        for r in range(1, m+1):
            for c in range(1, n+1):
                self.p_sum[r][c] = (self.p_sum[r-1][c] + self.p_sum[r][c-1] - 
                                    self.p_sum[r-1][c-1] + matrix[r-1][c-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2 = row1 + 1, row2 + 1
        c1, c2 = col1 + 1, col2 + 1
        return (self.p_sum[r2][c2] - self.p_sum[r2][c1-1] - 
                self.p_sum[r1-1][c2]+ self.p_sum[r1-1][c1-1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)