"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Store old to new pairs
        old_new = {}
        
        # Run BFS
        q = deque([node])
        while q:
            cur_node = q.popleft()
            if cur_node not in old_new:
                old_new[cur_node] = Node(cur_node.val)
                
            for nei in cur_node.neighbors:
                if nei not in old_new:
                    old_new[nei] = Node(nei.val)
                    q.append(nei)
                # Don't forget neighbors of current node's copy
                old_new[cur_node].neighbors.append(old_new[nei])
                
        return old_new[node]