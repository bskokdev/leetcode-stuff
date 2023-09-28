class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0
        for i in range(len(accounts)):
            localSum = 0
            for j in range(len(accounts[i])):
                localSum += accounts[i][j]
            maxSum = max(maxSum, localSum)
        return maxSum

                
