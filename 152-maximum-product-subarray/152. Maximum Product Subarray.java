class Solution {
    public int maxProduct(int[] nums) {
        // Overall approach is an extended version of Kaden's
        // because of negative numbers we have to maintain both current min & max
        int res = nums[0];
        for (int i = 1, curMin = res, curMax = res; i < nums.length; i++) {
            // negative num product (curMax would be < curMin) => we swap them
            if (nums[i] < 0) {
                int temp = curMin;
                curMin = curMax;
                curMax = temp;
            }
            
            // maintain current min & max values
            // same as in Kaden's but with 2 current trackers
            curMin = Math.min(nums[i], nums[i] * curMin);
            curMax = Math.max(nums[i], nums[i] * curMax);
            res = Math.max(res, curMax);
        }
        return res;
    }
}