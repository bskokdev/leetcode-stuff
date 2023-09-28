class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res, stack = [0] * n, []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                cur_idx = stack.pop()
                res[cur_idx] = i - cur_idx
            stack.append(i)
        return res

