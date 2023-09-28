class MinStack:

    def __init__(self):
        self.s = []
        self.s2 = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.s2 or val <= self.s2[-1]:
            self.s2.append(val)

    def pop(self) -> None:
        removed = self.s.pop()
        if self.s2[-1] == removed:
            self.s2.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()