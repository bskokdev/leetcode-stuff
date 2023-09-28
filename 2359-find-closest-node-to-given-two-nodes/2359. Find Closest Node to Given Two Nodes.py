class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = defaultdict(list)
        for src, dest in enumerate(edges):
            if dest == -1:
                continue
            graph[src].append(dest)

        def bfs(node, cur_distances):
            q = deque([(node, 0)])
            while q:
                cur_node, cur_dist = q.popleft()
                for nei in graph[cur_node]:
                    if nei not in cur_distances:
                        cur_distances[nei] = cur_dist + 1
                        q.append((nei, cur_dist + 1))

        bfs1_dist = {node1: 0}
        bfs2_dist = {node2: 0}
        bfs(node1, bfs1_dist)
        bfs(node2, bfs2_dist)

        res = -1
        res_dist = float('inf')
        for i in range(len(edges)):
            if i in bfs1_dist and i in bfs2_dist:
                cur_node_dist = max(bfs1_dist[i], bfs2_dist[i])
                if cur_node_dist < res_dist:
                    res = i
                    res_dist = cur_node_dist
        return res

