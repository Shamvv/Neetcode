from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = Counter((num % k + k) % k for num in arr)  
        for r in range(k):
            if r == 0: 
                if remainder_count[r] % 2 != 0:
                    return False
            elif r * 2 == k:  
                if remainder_count[r] % 2 != 0:
                    return False
            else:  
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        
        return True

        