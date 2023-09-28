class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # store map of [prev, prev_prev] indexes for each char
        # len(substring) == num of unique chars
        # -> we need to get the length between repeating chars
        pos = defaultdict(lambda: [-1, -1])
        ans = cur = 0
        for i, char in enumerate(s):
            cur += (i - pos[char][0]) - (pos[char][0] - pos[char][1])
            pos[char][1] = pos[char][0] 
            pos[char][0] = i
            ans += cur
        return ans