class Solution:
    # O(4^n) - at most we have 4 choices (num 7, 9), n -> recursion stack
    def generate_mapping(self):
        return {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        n = len(digits)
        mapping = self.generate_mapping()
        def dfs(i, cur_combination):
            if i >= n:
                res.append(cur_combination[:])
                return
            for char in mapping[digits[i]]:
                cur_combination += char
                dfs(i+1, cur_combination)
                cur_combination = cur_combination[:-1]
        dfs(0, "")
        return res