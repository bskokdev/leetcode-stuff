class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides, side_sum = [0] * 4, sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i >= len(matchsticks):
                return True
            for j in range(4):
                sides[j] += matchsticks[i]
                if sides[j] <= side_sum and dfs(i+1):
                    return True
                sides[j] -= matchsticks[i]
                if sides[j] == 0:
                    break
            return False
        return dfs(0)
        