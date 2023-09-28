class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        odds = 0
        for _, occ in counts.items():
          if occ % 2:
            odds += 1
        # we can build palindrome with all letters
        # odd count == 1 allows this ('aabaa')
        if odds <= 1:
          return len(s)
        # we can't build a palindrome with odd freq > 1
        # we have to remove odd freq letters and only use 1 of them
        return len(s) - odds + 1