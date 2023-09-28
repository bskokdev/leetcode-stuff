class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            String temp = expandAndReturn(i, i, s);
            if (temp.length() > res.length()) {
                res = temp;
            }
            temp = expandAndReturn(i, i+1, s);
            if (temp.length() > res.length()) {
                res = temp;
            }
        }
        return res;
    }

    private String expandAndReturn(int l, int r, String s) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return s.substring(l+1, r);
    }
}