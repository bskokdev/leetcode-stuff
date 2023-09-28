class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []
        for num, count in count.most_common(k):
            ans.append(num)
        return ans

        