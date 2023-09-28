class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == 'C' and stack:
                stack.pop()
            elif op == 'D' and stack:
                prev = stack[-1]
                stack.append(prev * 2)
            elif op == '+' and len(stack) >= 2:
                a, b = stack[-1], stack[-2]
                stack.append(a+b)
            else:
                stack.append(int(op))
        return sum(stack)
        

                    