class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int left = 0;
        int res = 0;
        int mostFrequentOcc = 0;
        for (int right = 0; right < s.length(); right++) {
            count[s.charAt(right) - 'A']++;
            mostFrequentOcc = Math.max(mostFrequentOcc, count[s.charAt(right) - 'A']);
            if ((right-left+1) - mostFrequentOcc > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }
            res = Math.max(right-left+1, res);
        }
        return res;
    }
}