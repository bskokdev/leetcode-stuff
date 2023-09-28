class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        pq = [(-freq, char) for char, freq in c.items()]
        heapq.heapify(pq)
        ans = ""
        prev = (0, '')
        while pq:
            cur_freq, cur_char = heapq.heappop(pq)
            ans += cur_char
            cur_freq += 1
            if prev[0] < 0:
                heapq.heappush(pq, prev)
            prev = (cur_freq, cur_char)
        if len(ans) != len(s):
            return ""
        return ans
