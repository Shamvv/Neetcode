class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.values():
                continue
            else:
                d[i] = nums[i]
        
        for i in range(len(nums)):
            if i in d:
                continue
            else:
                nums[i] = 101
                nums.append(0)
        while 101 in nums:
            nums.remove(101)
        return len(d)