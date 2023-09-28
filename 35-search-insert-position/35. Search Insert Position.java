class Solution {
    public int searchInsert(int[] nums, int target) {
        // find the first position from the left where nums[mid] >= target
        int left = 0;
        int right = nums.length;
        while (left < right) {
            int mid = (left + right ) >>> 1;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}