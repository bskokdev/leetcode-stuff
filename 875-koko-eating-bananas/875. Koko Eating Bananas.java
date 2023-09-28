class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1;
        int hi = Integer.MIN_VALUE;
        for (int pile : piles) {
            hi = Math.max(hi, pile);
        }
        int res = hi;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            int midTime = 0;
            for (int pile : piles) {
                midTime += Math.ceil((double)pile/mid);
            }
            if (midTime > h) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}