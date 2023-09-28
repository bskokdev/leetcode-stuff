class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        n = len(s)
        memo = {}
        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            res = 1 + dfs(i+1)
            for j in range(i, n):
                if s[i:j+1] in words:
                    res = min(res, dfs(j+1))
            memo[i] = res
            return res
        return dfs(0)