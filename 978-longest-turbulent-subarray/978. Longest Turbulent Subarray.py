class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        l = res = 0
        r = 1
        while r < n:
            while l < n-1 and arr[l] == arr[l+1]:
                l += 1
            while r < n-1 and (arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
                r += 1
            res = max(res, r-l+1)
            l = r
            r += 1
        return res
                
