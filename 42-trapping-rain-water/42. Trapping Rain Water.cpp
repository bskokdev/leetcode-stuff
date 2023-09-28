class Solution {
public:
  int trap(vector<int> &height) {
    int ans = 0;
    if (height.size() <= 0) {
      return ans;
    }
    int l = 0, r = height.size() - 1;
    int leftMax = height[l], rightMax = height[r];
    // water[i] == min(leftMax, rightMax) - height[i]; i is left or right pointer
    while (l < r) {
      // min(leftMax, rightMax) == leftMax
      if (leftMax < rightMax) {
        l++;
        leftMax = max(leftMax, height[l]);
        ans += leftMax - height[l];
        // min(leftMax, rightMax) == rightMax
      } else {
        r--;
        rightMax = max(rightMax, height[r]);
        ans += rightMax - height[r];
      }
    }
    return ans;
  }
};