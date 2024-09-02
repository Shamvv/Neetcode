class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            else:
                res.append(nums1[i])
                res.append(nums2[j])
                i += 1
                j += 1
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        l = len(res)
        if l == 1:
            return res[0]
        elif l == 2:
            return (res[0] + res[1]) / 2
        l, r = 0, len(res) - 1
        while l <= r:
            m = (l + r) // 2
            if len(res) % 2 == 1:
                return res[m]
            else:
                return ((res[m] + res[m + 1])/2)