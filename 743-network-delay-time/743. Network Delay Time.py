class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        cost = [float('inf')] * (n+1)
        cost[k] = 0

        pq = [(0, k)]
        heapq.heapify(pq)
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if cost[cur_node] < cur_cost:
                continue
            
            for nei, nei_cost in graph[cur_node]:
                new_nei_cost = nei_cost + cur_cost
                if new_nei_cost < cost[nei]:
                    cost[nei] = new_nei_cost
                    heapq.heappush(pq, (new_nei_cost, nei))
        res = max(cost[1:])
        return -1 if res == float('inf') else res
        