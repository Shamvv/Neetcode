class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        ml, tl = 0, 0
        for i in range(len(nums)):
            if nums[i] != k:
                if tl > ml:
                    ml = tl
                tl = 0
            else:
                tl += 1
        if tl > ml:
            ml = tl
        return ml