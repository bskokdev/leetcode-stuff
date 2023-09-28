class Solution:
    def get_adj(self, lock):
        res = []
        for i in range(len(lock)):
            up = str((int(lock[i])+1) % 10)
            res.append(lock[:i] + up + lock[i+1:])
            down = str((int(lock[i]) - 1 + 10) % 10)
            res.append(lock[:i] + down + lock[i+1:])
        return res
        
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
        q = deque([("0000", 0)])
        while q:
            lock, steps = q.popleft()
            if lock == target:
                return steps
            for adj in self.get_adj(lock):
                if adj not in visited:
                    visited.add(adj)
                    q.append((adj, steps+1))
        return -1
        