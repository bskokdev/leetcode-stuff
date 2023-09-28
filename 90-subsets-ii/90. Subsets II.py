class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        We keep track of generated subset frequencies in a set
        if the subset has been seen -> don't add it to the res list
        """
        res = []
        seen = set()
        def dfs(i, cur_comb):
            if i >= len(nums):
                subset_key = tuple(sorted(cur_comb))
                if subset_key not in seen:
                    res.append(cur_comb[:])
                    seen.add(subset_key)
                return
            
            # we add nums[i]
            cur_comb.append(nums[i])
            dfs(i+1, cur_comb)
            cur_comb.pop()

            # we don't add nums[i]
            dfs(i+1, cur_comb)
            
        dfs(0, [])
        return res