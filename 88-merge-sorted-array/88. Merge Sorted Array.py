class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # easier solution would be to add ans2 to ans1 and then sort it -> O(n log n)
        # or just use extra memory and two pointers from the front
        # create pointers at end indexes
        k = m+n-1
        i = m-1
        j = n-1
        # we want to iterate over the entire nums2 list
        while j >= 0:
            # if val in first array is bigger -> we take it
            # else we take val from the second array
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            