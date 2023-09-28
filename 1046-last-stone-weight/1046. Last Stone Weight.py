class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)

        while len(pq) >= 2:
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)
            if y == x:
                continue
            if y != x:
                heapq.heappush(pq, -(y-x))
        
        return -pq[0] if len(pq) == 1 else 0