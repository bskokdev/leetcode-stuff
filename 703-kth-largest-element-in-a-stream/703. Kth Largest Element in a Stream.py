class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        # if length of the pq is greater than k we remove the smallest el. from the PQ
        # we are then left with a PQ of size K
        # the Kth largest element is the first el. in min heap of size K
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)