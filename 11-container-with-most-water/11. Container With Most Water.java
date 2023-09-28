class Solution {
    public int maxArea(int[] height) {
        int res = Integer.MIN_VALUE;
        int left = 0;
        int right = height.length - 1;
        while(left < right) {
            int a = Math.min(height[left], height[right]);
            int b = right - left;
            int area = a * b;
            res = Math.max(res, area);
            if(height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
        }
        return res;
    }
}