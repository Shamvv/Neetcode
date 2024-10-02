class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = list(set(arr))
        s.sort()
        d = {}
        for i, j in enumerate(s):
            d[j] = i + 1
        for i, j in enumerate(arr):
            arr[i] = d[j]
        return arr