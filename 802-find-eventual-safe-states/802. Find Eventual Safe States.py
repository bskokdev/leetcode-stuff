class Solution: 
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n, g = len(graph), {}
        for i in range(n):
            g[i] = graph[i]

        visited, path = set(), set()
        def has_cycle(node):
            if node in path:
                return True
            if node in visited:
                return False
            visited.add(node)
            path.add(node)
            for nei in g[node]:
                if has_cycle(nei):
                    return True
            path.remove(node)
            return False
        
        res = []
        for i in range(n):
            if not has_cycle(i):
                res.append(i)
        return sorted(res)

        