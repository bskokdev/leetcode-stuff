class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n, res = len(s), []
        def is_palindrome(string):
            l, r = 0, len(string)-1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, cur_partition):
            if i == n:
                res.append(cur_partition[:])
                return
            for j in range(i, n):
                substr = s[i:j+1]
                if is_palindrome(substr):
                    cur_partition.append(substr)
                    dfs(j+1, cur_partition)
                    cur_partition.pop()
        dfs(0, [])
        return res

        