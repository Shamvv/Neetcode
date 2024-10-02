class Solution:
    def countAsterisks(self, s: str) -> int:
        p = 0
        a = 0
        for i in s:
            if i == "|" and p == 0:
                p = 1
            elif i == "|" and p == 1:
                p = 0
            if p == 0 and i == "*":
                a += 1
        return a