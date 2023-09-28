class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # at most 5 items -> O(5) sum
        v_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        left = res = 0
        for right in range(len(s)):
            if s[right] in v_count:
                v_count[s[right]] += 1
            if (right-left+1) > k:
                if s[left] in v_count:
                    v_count[s[left]] -= 1
                left += 1
            res = max(res, sum(v_count.values()))
        return res