class Solution {
    private int[][] memo;

    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        memo = new int[n][n];
        for (int[] row : memo) {
            Arrays.fill(row, Integer.MAX_VALUE);
        } 
        return dfs(0, 0, triangle);
    }

    private int dfs(int i, int j, List<List<Integer>> triangle) {
        if (memo[i][j] != Integer.MAX_VALUE) {
            return memo[i][j];
        }
        int cur = triangle.get(i).get(j);
        if (i == triangle.size() - 1) {
            return cur;
        }

        return memo[i][j] = cur + Math.min(dfs(i+1, j, triangle), dfs(i+1, j+1, triangle));
    }
}