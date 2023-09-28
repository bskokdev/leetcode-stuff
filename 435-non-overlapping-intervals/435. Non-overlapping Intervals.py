class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        prev_end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # there's an overlap
            if start < prev_end:
                count += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end
        return count
        