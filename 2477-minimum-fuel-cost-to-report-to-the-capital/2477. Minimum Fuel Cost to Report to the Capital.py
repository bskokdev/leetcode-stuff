class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        self.res = 0
        def dfs(node, parent):
            people = 0
            for nei in graph[node]:
                # prevent going back in an acyclic graph
                if nei != parent:
                    p = dfs(nei, node)
                    people += p
                    self.res += int(ceil(p/seats))
            return people + 1
        dfs(0, 0)
        return self.res