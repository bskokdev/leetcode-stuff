class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int left = 0;
        int right = 0;
        for (int w : weights) {
            left = Math.max(left, w);
            right += w;
        }
        while (left < right) {
            int mid = (left + right) >>> 1;
            if (ok(mid, weights, days)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    
    private boolean ok(int shipCapacity, int[] weights, int maxDays) {
        int sum = 0;
        int curDays = 1;
        for (int w : weights) {
            sum += w;
            if (sum > shipCapacity) {
                curDays++;
                sum = w;
            }
            if (curDays > maxDays) {
                return false;
            }
        }
        return true;
    }
}