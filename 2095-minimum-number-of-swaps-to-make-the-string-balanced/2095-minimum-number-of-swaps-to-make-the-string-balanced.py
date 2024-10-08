class Solution:
    def minSwaps(self, s: str) -> int:
        b, ib = 0, 0
        for i in s:
            if i == "[":
                b += 1
            else:
                b -= 1
            if b < 0:
                ib += 1
                b = 0
        return (ib + 1) // 2

        