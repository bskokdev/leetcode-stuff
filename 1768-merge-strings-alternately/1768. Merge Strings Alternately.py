class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        first_word = True
        j, k = 0, 0
        while j < len(word1) and k < len(word2):
            if first_word:
                ans += word1[j]
                j += 1
                first_word = False
            else:
                first_word = True
                ans += word2[k]
                k += 1

        while j < len(word1):
            ans += word1[j]
            j += 1
        while k < len(word2):
            ans += word2[k]
            k += 1
        return ans