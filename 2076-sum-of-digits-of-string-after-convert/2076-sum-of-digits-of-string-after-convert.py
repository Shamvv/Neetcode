class Solution:
    def getLucky(self, s: str, k: int) -> int:
        conv = ""
        a = "abcdefghijklmnopqrstuvwxyz"
        res = 0
        for i in s:
            conv += str(a.index(i) + 1)
        while k > 0:
            res = 0
            for i in conv:
                res += int(i)
            conv = str(res)
            k -= 1
        return res