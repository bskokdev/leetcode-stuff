class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(set))
        red, blue = True, False
        for src, dst in redEdges: graph[src][red].add(dst)
        for src, dst in blueEdges: graph[src][blue].add(dst)

        q = deque([(0, red), (0, blue)])
        level, res = 0, [float('inf')] * n
        while q:
            for _ in range(len(q)):
                node, color = q.popleft()
                res[node] = min(res[node], level)
                opp_col = color^1
                for nei in list(graph[node][opp_col]):
                    graph[node][opp_col].remove(nei)
                    q.append((nei, opp_col))
            level += 1
        return [r if r != float('inf') else -1 for r in res]
