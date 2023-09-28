class Solution {
    public boolean isValidSudoku(char[][] board) {
        // create set of strings
        // if pos is '.' skip
        // else create a hashes

        Set<String> set = new HashSet<>();
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                if(board[i][j] != '.') {
                    String curr = "[" + board[i][j] + "]";
                    if(!set.add(i + curr) || !set.add(curr + j) || !set.add(i/3 + curr + j/3)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}