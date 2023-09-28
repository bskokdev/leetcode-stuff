class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        g_min, res = prices[0], 0
        for i in range(1, len(prices)):
            res = max(prices[i] - g_min, res)
            g_min = min(g_min, prices[i])
        return res
        