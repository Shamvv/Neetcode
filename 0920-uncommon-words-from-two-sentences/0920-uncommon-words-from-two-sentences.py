class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        s = s1 + s2
        res = []
        for i in s:
            if s.count(i) == 1:
                res.append(i)
        return res
