class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        stack = [source]
        seen = set()
        while stack:
            cur = stack.pop()
            if cur == destination:
                return True
            
            for nei in graph[cur]:
                if nei not in seen:
                    stack.append(nei)
                    seen.add(nei)
        return False

