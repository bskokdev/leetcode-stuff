class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open, closed, cur_comb):
            if open == closed == n:
                res.append(cur_comb)
                return
            if open < n:
                dfs(open + 1, closed, cur_comb + "(")
            if open >= n or closed < open:
                dfs(open, closed + 1, cur_comb + ")")
        dfs(0, 0, "")
        return res
