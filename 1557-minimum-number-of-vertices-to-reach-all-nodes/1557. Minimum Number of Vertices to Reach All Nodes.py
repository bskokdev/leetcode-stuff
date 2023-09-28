class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        for _, dst in edges:
            in_degree[dst] += 1

        res = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                res.append(i)
        return res
        