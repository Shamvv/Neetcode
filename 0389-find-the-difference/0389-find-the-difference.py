class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_ = list(s)
        t_ = list(t)
        s_.sort()
        t_.sort()
        s = ""
        for i in s_:
            s += i
        s += "1"
        t = ""
        for i in t_:
            t += i
        for i, j in zip(s, t):
            print(i,j)
            if i != j:
                return j