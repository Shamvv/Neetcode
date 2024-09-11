class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start, goal = list(bin(start)[2:]), list(bin(goal)[2:])
        while len(start) != len(goal):
            if len(start) < len(goal):
                start.insert(0, '0')
            else:
                goal.insert(0, '0')
        start, goal = start[::-1], goal[::-1]
        res, i = 0, 0
        while start != goal and res < len(start):
            if start[i] != goal[i]:
                start[i] = goal[i]
                res += 1    
            i += 1
        return res
                