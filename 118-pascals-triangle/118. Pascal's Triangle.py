class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * (i + 1) for i in range(numRows)]
        for r in range(2, numRows):
            for c in range(1, r):
                dp[r][c] = dp[r-1][c-1] + dp[r-1][c]
        return dp
                

        
        