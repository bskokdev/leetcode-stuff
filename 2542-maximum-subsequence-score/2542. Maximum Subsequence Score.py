class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1_sum = res = 0
        pq = []
        for n1, n2 in sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True):
            n1_sum += n1
            heapq.heappush(pq, n1)
            if len(pq) > k:
                n1_popped = heapq.heappop(pq)
                n1_sum -= n1_popped
            if len(pq) == k:
                res = max(res, n1_sum * n2)
        return res
            

