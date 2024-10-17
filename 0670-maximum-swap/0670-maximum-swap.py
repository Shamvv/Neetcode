class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        
        for i in range(len(digits)):
            for d in range(9, int(digits[i]), -1):
                if d in last and last[d] > i:
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    return int(''.join(digits))
        
        return num

        