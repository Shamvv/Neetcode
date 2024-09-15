class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vtb = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        fc = {0:-1}
        bitmask, m = 0, 0
        for ind, char in enumerate(s):
            if char in vtb:
                bitmask ^= (1 << vtb[char])    
            if bitmask in fc:
                m = max(m, ind - fc[bitmask])
            else:
                fc[bitmask] = ind
        return m
        