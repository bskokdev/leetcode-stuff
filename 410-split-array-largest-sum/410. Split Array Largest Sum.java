class Solution {
    public int splitArray(int[] nums, int k) {
        int left = 0;
        int right = 0;
        for (int num : nums) {
            left = Math.max(left, num);
            right += num;
        }
        while (left < right) {
            int mid = (left + right) >>> 1;
            if (ok(mid, nums, k)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean ok(int treshold, int[] nums, int k) {
        int sum = 0;
        int kTaken = 1;
        for (int num : nums) {
            sum += num;
            if (sum > treshold) {
                kTaken++;
                sum = num;
                if (kTaken > k) {
                    return false;
                }
            }
        }
        return true;
    }
}