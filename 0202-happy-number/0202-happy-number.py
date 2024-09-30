class Solution:
    def digit_sum(self, n: int) -> int:
        s = 0
        while n != 0:
            s += (n % 10)**2
            n //= 10
        return s

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.digit_sum(n)
        return n == 1
