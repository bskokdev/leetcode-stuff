class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        count = 0
        while q:
            count += 1
            cur_node = q.popleft()
            for adj in graph[cur_node]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    q.append(adj)
                    
        return count == numCourses
        
