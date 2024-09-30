class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        curidx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[curidx] = nums[i]
                curidx += 1
        return curidx
