class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in mp:
                return [i, mp[rem]]
            mp[num] = i
        return -1