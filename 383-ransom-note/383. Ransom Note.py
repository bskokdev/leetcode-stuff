class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        note_count = Counter(ransomNote)

        for char in ransomNote:
            if char not in mag_count:
                return False
            if mag_count[char] < note_count[char]:
                return False
        return True
