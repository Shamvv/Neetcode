class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        c = 0
        if f == [0]:
            return True
        if f[0] == 0 and f[1] == 0:
            f[0] = 1
            c += 1  
        if f[-1] == 0 and f[-2] == 0:
            f[-1] = 1
            c += 1        
        for i in range(0, len(f) - 1):
            if f[i - 1] == 0 and f[i + 1] == 0 and f[i] == 0:
                f[i] = 1
                c += 1
        return c >= n
        