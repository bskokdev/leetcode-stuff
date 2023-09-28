class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}
        def dfs(cur_sum):
            if cur_sum in memo:
                return memo[cur_sum]
            if cur_sum < 0:
                return -1
            if cur_sum == 0:
                return 0

            min_used = float('inf')
            for coin in coins:
                cur_used = dfs(cur_sum - coin)
                if cur_used >= 0 and cur_used < min_used:
                    min_used = 1 + cur_used

            if min_used == float('inf'):
                memo[cur_sum] = -1
                return memo[cur_sum]

            memo[cur_sum] = min_used
            return memo[cur_sum]
            
        return dfs(amount)

