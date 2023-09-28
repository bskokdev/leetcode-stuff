class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) seen.add(num);
        int res = 0;
        for (int num : nums) {
            // we found end of a sequence
            if (!seen.contains(num+1)) {
                int j = 1;
                while (seen.contains(num-1)) {
                    j++;
                    num--;
                }
                res = Math.max(j, res);
            }
        }
        return res;
    }
}