class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = res = 0
        for i in range(k):
            s += arr[i]
        if s / k >= threshold:
            res += 1
        left = 0
        for right in range(k, len(arr)):
            s += arr[right] - arr[left]
            left += 1
            cur_avg = s / k
            if cur_avg >= threshold:
                res += 1
        return res
        
        