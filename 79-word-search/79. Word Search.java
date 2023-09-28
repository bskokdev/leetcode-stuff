class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        boolean[][] seen = new boolean[m][n];
        int[][] dirs = new int[][] {{0,1}, {1,0}, {0,-1}, {-1,0}};
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (dfs(r, c, board, 0, word, seen, dirs)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(int r, int c, char[][] board, int i, String word, boolean[][] seen, int[][] dirs) {
        // we went throught the entire word == it's in the grid
        if (i == word.length()) {
            return true;
        }
        // coordinates out of bounds
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length) {
            return false;
        }
        // coordinates already seen or they don't match the char
        if (seen[r][c] || board[r][c] != word.charAt(i)) {
            return false;
        }

        seen[r][c] = true;
        for (int[] dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            if (dfs(nr, nc, board, i+1, word, seen, dirs)) {
                return true;
            }
        }
        seen[r][c] = false;
        return false;
    }
}