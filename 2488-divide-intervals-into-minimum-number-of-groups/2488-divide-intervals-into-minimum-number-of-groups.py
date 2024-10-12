class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        
        for left, right in intervals:
            events.append((left, 'start'))
            events.append((right + 1, 'end'))
        
        events.sort(key=lambda x: (x[0], x[1] == 'start'))
        
        active_intervals = 0
        max_groups = 0
        
        for event in events:
            if event[1] == 'start':
                active_intervals += 1
                max_groups = max(max_groups, active_intervals)
            else:
                active_intervals -= 1
        
        return max_groups
