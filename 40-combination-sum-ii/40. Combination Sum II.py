class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def dfs(i, rem, path):
            if rem < 0:
                return
            if rem == 0:
                res.append(path[:])
                return
            
            for j in range(i, n):
                # handle duplicates in sorted list
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                dfs(j+1, rem - candidates[j], path)
                path.pop()

        dfs(0, target, [])
        return res