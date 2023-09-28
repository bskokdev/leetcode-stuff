class Solution {
    public int findClosestNumber(int[] nums) {
        int minDistanceToZero = Integer.MAX_VALUE;
        for (int num : nums) {
            if (Math.abs(num) < Math.abs(minDistanceToZero) || num == Math.abs(minDistanceToZero)) {
                minDistanceToZero = num;
            }
        }
        return minDistanceToZero;
    }
}