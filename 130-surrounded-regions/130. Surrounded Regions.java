class Solution {
    public void solve(char[][] board) {
        int m = board.length;
        int n = board[0].length;

        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') dfs(i, 0, board);
            if (board[i][n-1] == 'O') dfs(i, n-1, board);
        }

        for (int i = 0; i < n; i++) {
            if (board[0][i] == 'O') dfs(0, i, board);
            if (board[m-1][i] == 'O') dfs(m-1, i, board);
        }

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (board[r][c] == '#') {
                    board[r][c] = 'O';
                } else {
                    board[r][c] = 'X';
                }
            }
        }
    }

    private void dfs(int row, int col, char[][] grid) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length) {
            return;
        }
        if (grid[row][col] == 'X' || grid[row][col] == '#') {
            return;
        }
        grid[row][col] = '#';
        dfs(row+1, col, grid);
        dfs(row-1, col, grid);
        dfs(row, col+1, grid);
        dfs(row, col-1, grid);
    }
}