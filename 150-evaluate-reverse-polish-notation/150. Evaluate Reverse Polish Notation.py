class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(a, b, op):
            if op == "+":
                return a + b
            if op == "-":
                return a - b
            if op == "*":
                return a * b
            if op == "/":
                return a / b

        stack = []
        for token in tokens:
            # care stack len
            if token == "+" or token == "-" or token == "*" or token == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(evaluate(b, a, token))
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]

        