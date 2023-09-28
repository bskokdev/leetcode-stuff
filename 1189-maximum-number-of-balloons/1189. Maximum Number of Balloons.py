class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt_text = Counter(text)
        cnt_b = Counter('balloon')
        return min([cnt_text[c] // cnt_b[c] for c in cnt_b])
            

        