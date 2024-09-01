class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        original = list(original)
        original = original[::-1]
        if m * n != len(original):
            return []
        res = [[None for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                print(r, c)
                res[r][c] = original.pop()
        return res