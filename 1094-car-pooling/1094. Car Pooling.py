class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pd = defaultdict(int)
        for p, src, dst in trips:
            pd[src] += p
            pd[dst] -= p

        passengers = 0
        for key in sorted(pd.keys()):
            passengers += pd[key]
            if passengers > capacity:
                return False
        return True


        