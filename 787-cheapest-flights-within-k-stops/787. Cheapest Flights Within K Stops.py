class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # weighted directed graph representation
        graph = defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))
        # hahah TLE
        heap = [(0, src, k+1)]
        while heap:
            price, node, stops = heapq.heappop(heap)
            if stops >= 0 and node == dst:
                return price
                
            for neighbor, weight in graph[node]:
                if stops >= 0:
                    heapq.heappush(heap, (price+weight, neighbor, stops-1))
        return -1
