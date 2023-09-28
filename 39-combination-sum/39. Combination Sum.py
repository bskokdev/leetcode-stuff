class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def dfs(i, cur_comb, cur_sum):
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(cur_comb[:])
                return
            
            for j in range(i, n):
                cur_comb.append(candidates[j])
                dfs(j, cur_comb, cur_sum + candidates[j])
                cur_comb.pop()

        dfs(0, [], 0)
        return res