class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people)-1
        res = 0
        people.sort()
        while left <= right:
            cur_sum = people[left] + people[right]
            if cur_sum > limit:
                right -= 1
            else:
                right -= 1
                left += 1
            res += 1
        return res