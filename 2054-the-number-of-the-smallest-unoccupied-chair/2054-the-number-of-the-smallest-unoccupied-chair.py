import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        
        for friend_index, (arrival, leaving) in enumerate(times):
            events.append((arrival, 'arrive', friend_index))
            events.append((leaving, 'leave', friend_index))
        
        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))
        
        available_chairs = []
        next_chair = 0
        chair_assignment = [0] * len(times)
        
        for time, event_type, friend_index in events:
            if event_type == 'arrive':
                if available_chairs:
                    chair = heapq.heappop(available_chairs)
                else:
                    chair = next_chair
                    next_chair += 1
                
                chair_assignment[friend_index] = chair
                
                if friend_index == targetFriend:
                    target_chair = chair
            
            elif event_type == 'leave':
                chair = chair_assignment[friend_index]
                heapq.heappush(available_chairs, chair)
        
        return chair_assignment[targetFriend]