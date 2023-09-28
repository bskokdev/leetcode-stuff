class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        s1_count = Counter(s1)
        # get counts for initial window size
        s2_count = Counter(s2[:window_len-1])

        # keep track of the char counts in the hashmap rolling alongside the window
        # it's fixed size so we move left pointer and decrement count of left char each iteration
        # if count of the left char == 0 -> remove it from the hashmap
        left = 0
        for right in range(window_len-1, len(s2)):
            s2_count[s2[right]] += 1
            if s1_count == s2_count:
                return True
            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]
            left += 1
        return False

        