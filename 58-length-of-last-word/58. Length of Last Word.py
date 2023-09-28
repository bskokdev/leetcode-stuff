class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s)-1
        while s[r] == " " and r >= 0:
            r -= 1
        l = r - 1
        while s[l] != " " and l >= 0:
            l -= 1
        return r - l