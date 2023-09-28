class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return []
            
        mp = collections.defaultdict(list)
        for anagram in strs:
            sortedAnagram = ''.join(sorted(anagram))
            mp[sortedAnagram].append(anagram)

        groups = [group for group in mp.values()]
        return groups

        