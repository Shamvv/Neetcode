class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        d = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                d.append(i)        
        if len(d) == 2:
            return (s1[d[0]] == s2[d[1]] and s1[d[1]] == s2[d[0]])
        return False