class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window with set
        seen = set()
        left = res = 0
        for right in range(len(s)):
            if s[right] not in seen:
                res = max(res, right-left+1)
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(s[right])
        return res
            