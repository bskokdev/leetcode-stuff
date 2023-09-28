class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        cur = newInterval
        for interval in intervals:
            if interval[0] > cur[1]:
               res.append(cur)
               cur = interval
            elif cur[0] <= interval[1]:
                cur[0] = min(cur[0], interval[0])
                cur[1] = max(cur[1], interval[1])
            else:
                res.append(interval)
        res.append(cur)
        return res
