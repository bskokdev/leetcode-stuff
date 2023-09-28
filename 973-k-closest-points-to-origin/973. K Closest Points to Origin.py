class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (distance, [x, y])
        pq = []
        for point in points:
            # calculate eucl. distance from ith point to [0, 0] & add to the min heap
            distance = math.sqrt(math.pow(0 - point[0], 2) + math.pow(0 - point[1], 2))
            pq.append((distance, point))

        heapq.heapify(pq)
        ans = []
        while k:
            # append coordinates to the ans
            ans.append(heapq.heappop(pq)[1])
            k -= 1
        return ans
