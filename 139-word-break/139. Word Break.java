class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        Map<Integer, Boolean> memo = new HashMap<>();
        return dfs(0, s, dict, memo);
    }

    private boolean dfs(int i, String s, Set<String> dict, Map<Integer, Boolean> memo) {
        if (memo.containsKey(i)) {
            return memo.get(i);
        }
        if (i == s.length()) {
            return true;
        }

        for (int j = i+1; j < s.length()+1; j++) {
            String subStr = s.substring(i, j);
            if (dict.contains(subStr) && dfs(j, s, dict, memo)) {
                memo.put(i, true);
                return true;
            }
        }
        memo.put(i, false);
        return false;
    }
}