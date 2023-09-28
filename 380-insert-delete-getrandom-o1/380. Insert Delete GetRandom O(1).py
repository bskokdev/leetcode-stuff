class RandomizedSet:

    def __init__(self):
        self.data = []
        self.lookup = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False
        self.data.append(val)
        self.lookup[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.lookup:
            return False

        found_idx = self.lookup[val]
        self.data[found_idx], self.data[-1] = self.data[-1], self.data[found_idx]
        self.lookup[self.data[found_idx]] = found_idx
        
        self.size -= 1
        self.data.pop()
        del self.lookup[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()