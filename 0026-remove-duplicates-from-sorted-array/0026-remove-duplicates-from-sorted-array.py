class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = len(set(nums))
        while len(nums) != s:
            for i in nums:
                if nums.count(i) > 1:
                    nums.remove(i)
        return len(nums)