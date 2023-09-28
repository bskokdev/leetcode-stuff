class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = [-num for num in nums]
        heapq.heapify(pq)

        ans = float("-inf")
        while k:
            ans = -1 * heapq.heappop(pq)
            k -= 1
        return ans