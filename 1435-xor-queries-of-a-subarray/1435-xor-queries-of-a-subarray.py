class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]        
        for start, end in queries:
            if start == 0:
                res.append(arr[end])
            else:
                res.append(arr[end] ^ arr[start - 1])
        return res
