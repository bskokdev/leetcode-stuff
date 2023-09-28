class Solution:
    def three_sum(self, nums: List[int], target) -> List[List[int]]:
        # Here I would assume the nums list is already sorted
        ans = []
        # for each num in nums I need to find matching two sum
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                left, right = i + 1, len(nums) - 1
                new_target = target - nums[i]
                while left < right:
                    temp_sum = nums[left] + nums[right]
                    if temp_sum == new_target:
                        ans.append([nums[i], nums[left], nums[right]])
                        # skip left idx while it has the same values at left+1
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # skip right idx while it has the same values at right-1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif temp_sum < new_target:
                        left += 1
                    else:
                        right -= 1
        return ans


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return []
        ans = []
        nums.sort()
        for i in range(len(nums)):
            # prevent duplicate values
            if i == 0 or nums[i] != nums[i-1]:
                # pass in the nums list from i+1 to the end
                three_sum_res = self.three_sum(nums[i+1:], target-nums[i])
                for res in three_sum_res:
                    res.append(nums[i])
                    ans.append(res)
        return ans