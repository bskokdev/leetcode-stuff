class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            # opening bracket
            if char in mp:
                stack.append(char)
            else:
                # check if closing bracket matches the closing bracket of last opening bracket
                if stack:
                    last_opening = stack.pop()
                    if mp[last_opening] != char:
                        return False
                else:
                    return False
        return len(stack) == 0