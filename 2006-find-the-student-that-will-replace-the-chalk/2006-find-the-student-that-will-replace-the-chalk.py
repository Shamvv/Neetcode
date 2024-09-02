class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k %= s
        for kid in range(len(chalk)):
            if chalk[kid] > k:
                return kid
            k -= chalk[kid]