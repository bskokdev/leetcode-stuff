class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        bin0, bin1 = '', ''
        for i in range(2 * n):
            bin0 += '0' if i % 2 else '1'
            bin1 += '1' if i % 2 else '0'
        
        left = diff1 = diff2 = 0
        res = n
        for right in range(2 * n):
            if bin0[right] != s[right]:
                diff1 += 1
            if bin1[right] != s[right]:
                diff2 += 1
            if right-left+1 > n:
                if bin0[left] != s[left]:
                    diff1 -= 1
                if bin1[left] != s[left]:
                    diff2 -= 1
                left += 1
            if right-left+1 == n:
                res = min(res, diff1, diff2)
        return res
            