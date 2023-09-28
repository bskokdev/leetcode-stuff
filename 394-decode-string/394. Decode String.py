class Solution:
    def decodeString(self, s: str) -> str:
        # stack stores pair of (string, num - how many times it repeats)
        stack = [["", 1]]
        cur_num = ""
        for ch in s:
            if ch.isdigit():
                # the number could be more than 1 digit so we store a string
                cur_num += ch
            elif ch == "[":
                stack.append(["", int(cur_num)])
                cur_num = ""
            elif ch == "]":
                val, num = stack.pop()
                # we add the string num times to the top of the stack
                stack[-1][0] += val * num
            else:
                # else we keep building the string (this is in the brackets in the input)
                stack[-1][0] += ch
        # we return fully build string from the sub-strings
        return stack[-1][0]
