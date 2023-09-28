class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(0, nums, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int i, int[] nums, List<Integer> cur, List<List<Integer>> res) {
        int n = nums.length;
        if (i >= n) {
            res.add(new ArrayList<>(cur));
            return;
        }
        // take it
        cur.add(nums[i]);
        dfs(i+1, nums, cur, res);
        
        // don't take it
        cur.remove(cur.size()-1);
        dfs(i+1, nums, cur, res);
    }
}