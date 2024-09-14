class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        longest_length, current_length = 0, 0
        for i, j in enumerate(nums):
            if j == k:
                current_length += 1
                longest_length = max(current_length, longest_length)
            else:
                current_length = 0
        return longest_length