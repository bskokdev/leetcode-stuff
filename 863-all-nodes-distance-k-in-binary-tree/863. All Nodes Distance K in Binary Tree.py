# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convert_tree_to_graph(self, node, graph):
        if not node: return
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
            self.convert_tree_to_graph(node.left, graph)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
            self.convert_tree_to_graph(node.right, graph)
        

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root: return []

        graph = collections.defaultdict(list)
        self.convert_tree_to_graph(root, graph)

        queue = collections.deque([target.val])
        seen = set([target.val])
        while queue and k > 0:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for node in graph[cur]:
                    if node not in seen:
                        queue.append(node)
                        seen.add(node)
            k -= 1
        return list(queue)
        # convert root to a graph
        # run bfs from target node and decrement k
        # if k == 0 return queue (current level at distance k) as list

















