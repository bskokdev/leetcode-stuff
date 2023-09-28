class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      mp = defaultdict(int)
      n = len(s)
      for i in range(n):
        mp[s[i]] += 1
        mp[t[i]] -= 1
      
      for val in mp.values():
        if val != 0:
          return False
      return True
