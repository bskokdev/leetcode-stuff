class Solution:
    def romanToInt(self, s: str) -> int:
        a = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        n = len(s)
        res = 0
        for i in range(n-1):
            if a[s[i]] < a[s[i+1]]:
                res -= a[s[i]]
            else:
                res += a[s[i]]
        return res + a[s[n-1]]