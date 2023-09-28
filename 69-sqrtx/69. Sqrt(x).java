class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        int left = 1;
        int right = x;
        while (left < right) {
            int mid = (left + right) >>> 1;
            if (mid * mid <= x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left-1;
    }
}